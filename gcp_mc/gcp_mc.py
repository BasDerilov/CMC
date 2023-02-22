from pick import pick

from modules.palmsbet_mc.scripts.configure import configure_plugins, configure_server
from modules.palmsbet_mc.scripts.download_bins import download_deps


def main():
    
    # action = pick(["start-locally", "deploy-to-cloud"], "Choose server deployment action", default_index=0)
    

    download_deps()
    configure_server()
    configure_plugins()
    
    print("gcp_mc WORKS!")

