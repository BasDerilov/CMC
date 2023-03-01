"""gcp_mc is a tool for quicly spooling up minecraft servers locally or on Google Cloud
Platform

"""


from pick import pick
from minecraft import main as mc_server


def main():
    """The main entrypoint of gcp_mc"""
    action = pick(
        ["start-locally", "deploy-to-cloud"],
        "Choose server deployment action",
        default_index=0,
    )

    print(action)
    if action[1] == 0:
        mc_server()

    print("gcp_mc WORKS!")
