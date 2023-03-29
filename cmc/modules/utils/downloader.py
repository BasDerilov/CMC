from pathlib import Path
from threading import Event
from typing import Iterable
from functools import partial
from urllib.request import urlopen

import requests
from cmc.models import CmcPackageModel
from concurrent.futures import ThreadPoolExecutor
from .console import console, err_console

from rich.console import Console
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)


class Downloader:

    console: Console
    err_console: Console
    package: CmcPackageModel
    done_event: Event
    progress: Progress

    def __init__(
        self,
        package: CmcPackageModel,
        dw_console: Console = None,
        dw_err_console: Console = None,
    ) -> None:

        if dw_console is None:
            dw_console = console

        if dw_err_console is None:
            dw_err_console = err_console

        self.console = dw_console
        self.err_console = dw_err_console
        self.package = package
        self.progress = Progress(
            TextColumn(
                "{task.fields[filename]}",
                style=dw_console._theme_stack.get("info"),
            ),
            BarColumn(
                bar_width=None,
            ),
            "[progress.percentage]{task.percentage:>3.1f}%",
            "•",
            DownloadColumn(),
            "•",
            TransferSpeedColumn(),
            "•",
            TimeRemainingColumn(),
            console=dw_console,
        )

    def copy_url(self, task_id: TaskID, url: str, path: str) -> None:
        """Copy data from a url to a local file."""
        self.progress.console.log(f"Requesting {url}")
        response = urlopen(url)
        # This will break if the response doesn't contain content length
        self.progress.update(task_id, total=int(response.info()["Content-length"]))
        with open(path, "wb") as dest_file:
            self.progress.start_task(task_id)
            for data in iter(partial(response.read, 32768), b""):
                dest_file.write(data)
                self.progress.update(task_id, advance=len(data))

        self.progress.console.log(f"Downloaded {path}")

    def download(self, urls: Iterable[str], dest_dir: Path):
        """Download multiple files to the given directory."""

        with self.progress:
            with ThreadPoolExecutor(max_workers=4) as pool:
                for url in urls:
                    filename = url.split("/")[-1]
                    dest_path = dest_dir.joinpath(filename)
                    task_id = self.progress.add_task(
                        "download", filename=filename, start=False
                    )
                    pool.submit(self.copy_url, task_id, url, dest_path)

    def curse_download(self, slugs: Iterable[str], dest_dir: Path, curse_key: str):
        """Download multiple files to the given directory from the curse forge API."""
        headers = {"Accept": "application/json", "x-api-key": curse_key}

        responses = []
        for slug in slugs:

            responses.append(
                requests.get(
                    f"{self.package.api}/v1/mods/search",
                    params={"gameId": "432", "slug": slug},
                    headers=headers,
                    timeout=1000,
                )
            )

        results: list[tuple] = []
        for response, slug in zip(responses, slugs):

            if response.json()["pagination"]["resultCount"] == 0:

                console.print(
                    f'Curse resource "{slug}" returned 0 \
matches. Is this the correct slug?',
                    style="warning",
                )

            else:
                results.append((response, slug))
                console.print(
                    f"found curse resource {slug}",
                    style="info",
                )

        urls = []
        for result, slug in results:

            result_data = result.json()["data"][0]

            mod_id = result_data["id"]
            files_index: list = result_data["latestFilesIndexes"]

            if len(files_index) == 0:
                console.print(
                    f'"{slug}" has a bad API support, skipping',
                    style="warning",
                )
                continue

            file_id = next(
                (
                    x
                    for x in files_index
                    if x["gameVersion"] == self.package.game_version
                ),
                None,
            )["fileId"]

            if file_id is None:

                console.print(
                    f'"{slug}" doesn\'t support your version of minecraft \
{self.package.game_version}',
                    style="warning",
                )

                continue

            file_response = requests.get(
                f"{self.package.api}/v1/mods/{mod_id}/files/{file_id}",
                headers=headers,
                timeout=10000,
            )

            if file_response.status_code != 200:
                err_console.print(
                    f"curse resource file for {slug}\
                        returned status code {file_response.status_code}"
                )
                return

            file_response = file_response.json()
            urls.append(file_response["data"]["downloadUrl"])

        self.download(urls, dest_dir)
