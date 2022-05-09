# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/12 10:45
@Auth ： yinyi
@File ：Curl_Graphy.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from py2neo import Graph, Node


def connect():
    """
    :rtype: object
    """
    driver = Graph("bolt://localhost:7687", auth=("neo4j", "wei7wei"))
    return driver


def f(string1, string2):
    data_list = []
    session = connect()
    data = {}
    cql = "MATCH p=(a)-[*]->(b) where a.IP='"+string1+"'and b.IP='"+string2+"' RETURN p"
    print(cql)
    if cql != "":
        e = session.begin().run(cql).data()
        for i in range(len(e)):
            for key, val in e[i].items():
                nodes = val.nodes
                print(nodes)
                data = {"p": {
                    "start": {
                        "identity": nodes[0].identity,
                        "labels": [
                            nodes[0]["post"]
                        ],
                        "properties": {
                            "ip": nodes[0]["IP"],
                            "tiji": nodes[0]["num"],
                            "kind": nodes[0]["kind"],
                            "name": nodes[0]["post"]
                        }
                    },
                    "end": {
                        "identity": nodes[1].identity,
                        "labels": [nodes[1]["post"]],
                        "properties": {
                            "ip": nodes[1]["IP"],
                            "tiji": nodes[1]["num"],
                            "kind": nodes[1]["kind"],
                            "name": nodes[1]["post"]
                        }
                    },
                    "segments": [
                        {
                            "start": {
                                "identity": nodes[0].identity,
                                "labels": [
                                    nodes[0]["post"]
                                ],
                                "properties": {
                                    "ip": nodes[0]["IP"],
                                    "tiji": nodes[0]["num"],
                                    "kind": nodes[0]["kind"],
                                    "name": nodes[0]["post"]
                                }
                            },
                            "relationship": {
                                "identity": 66666,
                                "start": nodes[0].identity,
                                "end": nodes[1].identity,
                                "type": "type",
                                "properties": {
                                    "name": "指向"
                                }
                            },
                            "end": {
                                "identity": nodes[1].identity,
                                "labels": [nodes[1]["post"]],
                                "properties": {
                                    "ip": nodes[1]["IP"],
                                    "tiji": nodes[1]["num"],
                                    "kind": nodes[1]["kind"],
                                    "name": nodes[1]["post"]
                                }
                            }
                        }
                    ],
                    "length": 1.0
                }
                }
                data_list.append(data)
    return data_list


def getnode(string, shuxing) -> list:
    data_list = []
    session = connect()
    data = {}
    cql = ""
    if shuxing == "ip":
        cql = "match p=()-->(n),m=(n)-->() where n.IP='" + string + "' return p,m"
    elif shuxing == "post":
        cql = "match p=()-->(n),m=(n)-->() where n.post='" + string + "' return p,m"
    elif shuxing == "kind":
        cql = "match p=()-->(n),m=(n)-->() where n.kind='" + string + "' return p,m"
    if cql != "":
        e = session.begin().run(cql).data()
        for i in range(len(e)):
            for key, val in e[i].items():
                nodes = val.nodes
                print(nodes)
                data = {"p": {
                    "start": {
                        "identity": nodes[0].identity,
                        "labels": [
                            nodes[0]["post"]
                        ],
                        "properties": {
                            "ip": nodes[0]["IP"],
                            "tiji": nodes[0]["num"],
                            "kind": nodes[0]["kind"],
                            "name": nodes[0]["post"]
                        }
                    },
                    "end": {
                        "identity": nodes[1].identity,
                        "labels": [nodes[1]["post"]],
                        "properties": {
                            "ip": nodes[1]["IP"],
                            "tiji": nodes[1]["num"],
                            "kind": nodes[1]["kind"],
                            "name": nodes[1]["post"]
                        }
                    },
                    "segments": [
                        {
                            "start": {
                                "identity": nodes[0].identity,
                                "labels": [
                                    nodes[0]["post"]
                                ],
                                "properties": {
                                    "ip": nodes[0]["IP"],
                                    "tiji": nodes[0]["num"],
                                    "kind": nodes[0]["kind"],
                                    "name": nodes[0]["post"]
                                }
                            },
                            "relationship": {
                                "identity": 66666,
                                "start": nodes[0].identity,
                                "end": nodes[1].identity,
                                "type": "type",
                                "properties": {
                                    "name": "指向"
                                }
                            },
                            "end": {
                                "identity": nodes[1].identity,
                                "labels": [nodes[1]["post"]],
                                "properties": {
                                    "ip": nodes[1]["IP"],
                                    "tiji": nodes[1]["num"],
                                    "kind": nodes[1]["kind"],
                                    "name": nodes[1]["post"]
                                }
                            }
                        }
                    ],
                    "length": 1.0
                }
                }
                data_list.append(data)
    return data_list


def return_dict() -> list:
    driver = connect()
    data_list = []
    cql2 = "MATCH P=(N)-->(),M=()-->(N) RETURN P,M"
    e = driver.begin().run(cql2).data()
    for i in range(len(e)):
        for key, val in e[i].items():
            nodes = val.nodes
            data = {"p": {
                "start": {
                    "identity": nodes[0].identity,
                    "labels": [
                        nodes[0]["post"]
                    ],
                    "properties": {
                        "ip": nodes[0]["IP"],
                        "tiji": nodes[0]["num"],
                        "kind": nodes[0]["kind"],
                        "name": nodes[0]["post"]
                    }
                },
                "end": {
                    "identity": nodes[1].identity,
                    "labels": [nodes[1]["post"]],
                    "properties": {
                        "ip": nodes[1]["IP"],
                        "tiji": nodes[1]["num"],
                        "kind": nodes[1]["kind"],
                        "name": nodes[1]["post"]
                    }
                },
                "segments": [
                    {
                        "start": {
                            "identity": nodes[0].identity,
                            "labels": [
                                nodes[0]["post"]
                            ],
                            "properties": {
                                "ip": nodes[0]["IP"],
                                "tiji": nodes[0]["num"],
                                "kind": nodes[0]["kind"],
                                "name": nodes[0]["post"]
                            }
                        },
                        "relationship": {
                            "identity": 66666,
                            "start": nodes[0].identity,
                            "end": nodes[1].identity,
                            "type": "type",
                            "properties": {
                                "name": "指向"
                            }
                        },
                        "end": {
                            "identity": nodes[1].identity,
                            "labels": [nodes[1]["post"]],
                            "properties": {
                                "ip": nodes[1]["IP"],
                                "tiji": nodes[1]["num"],
                                "kind": nodes[1]["kind"],
                                "name": nodes[1]["post"]
                            }
                        }
                    }
                ],
                "length": 1.0
            }
            }
            data_list.append(data)
    return data_list

# if __name__ == '__main__':
# getnode("2001:da8:270:2020::1")
# return_dict()
