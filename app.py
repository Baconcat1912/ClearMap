from flask import Flask, request, render_template_string
import re
import networkx as nx
from pyvis.network import Network

app = Flask(__name__)
