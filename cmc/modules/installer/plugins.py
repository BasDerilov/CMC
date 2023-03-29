# TODO Implement new istaller module for plugins only
# NOTE assume the minecraft installer module is finished by now and there is
# a server folder

# NOTE concurrent file downloading would be nice
# NOTE IMPORTANT! Should also only work with the CmcPackageModel and CmcConfigModel

# NOTE I am writing this down because it's 2 AM and tommorow me wont remember shit and
# will probably create another dumpster fire.

from pathlib import Path
from cmc.models import CmcConfigModel, CmcPackageModel
from .console import err_console, console
from cmc.modules.utils import ensure_dirs, Downloader


class Plugins:

    package: CmcPackageModel
    config: CmcConfigModel
    downloader: Downloader

    def __init__(self, package: CmcPackageModel, config: CmcConfigModel) -> None:
        self.package = package
        self.config = config
        self.plugins_dir = Path(package.name).joinpath("plugins")
        self.downloader = Downloader(package, console, err_console)

    def install_from_urls(self):

        if len(self.package.url_plugins) == 0:
            console.log(
                "no plugins listed in cmc-package, none will be installed",
                style="info",
            )
            return

        console.rule(
            f'Installing "{self.package.name}" plugins from urls', style="info"
        )
        ensure_dirs(self.plugins_dir)

        self.downloader.download(self.package.url_plugins, self.plugins_dir)

    def install_from_curse(self, curse_key: str):

        if len(self.package.curse_plugins) == 0:
            console.log(
                "no curse plugins listed in cmc-package, none will be installed",
                style="curse",
            )
            return

        console.rule(
            f'Installing "{self.package.name}" plugins from curse api', style="curse"
        )
        ensure_dirs(self.plugins_dir)

        self.downloader.curse_download(
            self.package.curse_plugins, self.plugins_dir, curse_key
        )
