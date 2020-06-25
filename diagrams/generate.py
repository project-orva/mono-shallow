#!/usr/bin/python3.7.7
from urllib.request import urlretrieve

from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Pod
from diagrams.programming.framework import React

from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.database import PostgreSQL
from diagrams.custom import Custom

graphql_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/GraphQL_Logo.svg/200px-GraphQL_Logo.svg.png"
graphql_icon = "assets/graphql.png"
urlretrieve(graphql_url, graphql_icon)

orva_url = "https://avatars2.githubusercontent.com/u/53947571?s=200&v=4"
orva_icon = "assets/pr-orva.png"

phone_url = "https://cdn0.iconfinder.com/data/icons/devices-technologies/100/cellulare1-512.png"
phone_icon = "assets/phone.png"

voice_url = "https://cdn3.iconfinder.com/data/icons/google-material-design-icons/48/ic_keyboard_voice_48px-512.png"
voice_icon = "assets/voice.png"

urlretrieve(orva_url, orva_icon)
urlretrieve(phone_url, phone_icon)
urlretrieve(voice_url, voice_icon)

graph_attr = {
    "fontsize": "0",
    "bgcolor": "transparent"
}

with Diagram(name="Orva Architecture Overview", show=False, graph_attr=graph_attr):
    core = Custom("core", orva_icon)

    with Cluster("Client Devices"):
        devices = [
            Custom("phone", phone_icon),
            Custom("voice", voice_icon)
        ]
        devices >> core

    with Cluster("Auth"):
        auth = EC2("Auth")

    with Cluster("Database"):
        resository_ingress = EC2("Repository Ingress")

        resository_ingress >> [
            RDS("Profile"),
            RDS("Account"),
            auth,
        ]
        core >> [
            resository_ingress,
        ]

    with Cluster("Skills"):
        sk_1 = EC2("Skill 1")
        skills = [
            sk_1,
        ] >> resository_ingress

    with Cluster("gRPC Services"):
        skill = EC2("Skill Router")
        core >> [
            EC2("Speech"),
        ]
        core >> skill >> sk_1

    with Cluster("Web"):
        web = React("web app")

        web >> Custom("query service", graphql_icon) >> [
            core,
            resository_ingress,
        ]
        web >> auth
