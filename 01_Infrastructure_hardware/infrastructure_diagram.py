import pygraphviz as pgv

# Create a new directed graph
uml_diagram = pgv.AGraph(directed=True, rankdir='LR', size='10,8')

# Add components
uml_diagram.add_node("Server", label="Main Server")
uml_diagram.add_node("OS", label="Operating Systems\n(Linux, Windows Server)")

uml_diagram.add_node("WebServers", label="Web Servers\n(Nginx, Apache)")
uml_diagram.add_node("Databases", label="Databases\n(MySQL, PostgreSQL, MongoDB)")
uml_diagram.add_node("Containers", label="Containers\n(Docker, Kubernetes)")

uml_diagram.add_node("DataScience", label="Data Science Tools\n(Jupyter, RStudio)")
uml_diagram.add_node("DataEngineering", label="Data Engineering Tools\n(Hadoop, Spark)")

uml_diagram.add_node("AIFrameworks", label="AI/ML Frameworks\n(LLaMA, TensorFlow, PyTorch)")
uml_diagram.add_node("Governance", label="Data Governance\n(Cataloging, Quality, Compliance)")

uml_diagram.add_node("Backup", label="Backup System\n(Nextcloud)")
uml_diagram.add_node("MediaServer", label="Media Server\n(Jellyfin)")

uml_diagram.add_node("AIforBusiness", label="AI for Business\n(Chatbot, CRM Integration, Proposal Generation)")

# Define relationships
uml_diagram.add_edge("Server", "OS")
uml_diagram.add_edge("OS", "WebServers")
uml_diagram.add_edge("OS", "Databases")
uml_diagram.add_edge("OS", "Containers")
uml_diagram.add_edge("OS", "DataScience")
uml_diagram.add_edge("OS", "DataEngineering")
uml_diagram.add_edge("OS", "AIFrameworks")
uml_diagram.add_edge("OS", "Governance")
uml_diagram.add_edge("OS", "Backup")
uml_diagram.add_edge("OS", "MediaServer")
uml_diagram.add_edge("OS", "AIforBusiness")

# Save the diagram as an image
uml_diagram.draw("infrastructure_uml_diagram.png", prog="dot", format="png")