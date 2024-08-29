from graphviz import Digraph

# Create a new directed graph
uml_diagram = Digraph("Infrastructure UML", filename="infrastructure_uml_diagram", format="png")
uml_diagram.attr(rankdir='LR', size='10,8')

# Add components
uml_diagram.node("Server", "Main Server")
uml_diagram.node("OS", "Operating Systems\n(Linux, Windows Server)")

uml_diagram.node("WebServers", "Web Servers\n(Nginx, Apache)")
uml_diagram.node("Databases", "Databases\n(MySQL, PostgreSQL, MongoDB)")
uml_diagram.node("Containers", "Containers\n(Docker, Kubernetes)")

uml_diagram.node("DataScience", "Data Science Tools\n(Jupyter, RStudio)")
uml_diagram.node("DataEngineering", "Data Engineering Tools\n(Hadoop, Spark)")

uml_diagram.node("AIFrameworks", "AI/ML Frameworks\n(LLaMA, TensorFlow, PyTorch)")
uml_diagram.node("Governance", "Data Governance\n(Cataloging, Quality, Compliance)")

uml_diagram.node("Backup", "Backup System\n(Nextcloud)")
uml_diagram.node("MediaServer", "Media Server\n(Jellyfin)")

uml_diagram.node("AIforBusiness", "AI for Business\n(Chatbot, CRM Integration, Proposal Generation)")

# Define relationships
uml_diagram.edge("Server", "OS")
uml_diagram.edge("OS", "WebServers")
uml_diagram.edge("OS", "Databases")
uml_diagram.edge("OS", "Containers")
uml_diagram.edge("OS", "DataScience")
uml_diagram.edge("OS", "DataEngineering")
uml_diagram.edge("OS", "AIFrameworks")
uml_diagram.edge("OS", "Governance")
uml_diagram.edge("OS", "Backup")
uml_diagram.edge("OS", "MediaServer")
uml_diagram.edge("OS", "AIforBusiness")

uml_diagram.view()