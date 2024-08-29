import pygraphviz as pgv

# Create a new directed graph
uml_diagram = pgv.AGraph(directed=True, rankdir='TB', size='14,20', dpi=300)

# Add main components
uml_diagram.add_node("Infrastructure", shape="box", style="filled", fillcolor="#E6E6FA")
uml_diagram.add_node("OS", label="Operating Systems\n(Linux, Windows Server)", shape="box")
uml_diagram.add_node("Software", label="Software and Services", shape="box")
uml_diagram.add_node("DataAI", label="Data Science and AI", shape="box")
uml_diagram.add_node("Management", label="Monitoring and Management", shape="box")
uml_diagram.add_node("Governance", label="Data Governance", shape="box")
uml_diagram.add_node("MediaBackup", label="Media and Backup", shape="box")
uml_diagram.add_node("AIBusiness", label="AI for Business", shape="box")

# Add subcomponents
uml_diagram.add_node("WebServers", label="Web Servers\n(Nginx, Apache)")
uml_diagram.add_node("Databases", label="Databases\n(MySQL, PostgreSQL, MongoDB)")
uml_diagram.add_node("Containers", label="Containers\n(Docker, Kubernetes)")

uml_diagram.add_node("DataScience", label="Data Science Tools\n(Jupyter, RStudio, Anaconda)")
uml_diagram.add_node("DataEngineering", label="Data Engineering\n(Hadoop, Spark, Kafka)")
uml_diagram.add_node("AIFrameworks", label="AI/ML Frameworks\n(TensorFlow, PyTorch, LLaMA)")
uml_diagram.add_node("ContinuousLearning", label="Continuous Learning Pipeline")
uml_diagram.add_node("DocGeneration", label="Document Generation")

uml_diagram.add_node("Monitoring", label="Monitoring\n(Prometheus, Grafana, Zabbix)")
uml_diagram.add_node("ConfigManagement", label="Config Management\n(Ansible, Terraform)")
uml_diagram.add_node("BackupTools", label="Backup\n(Rsync, Bacula, Veeam)")

uml_diagram.add_node("DataGovFramework", label="Data Governance Framework")
uml_diagram.add_node("DataCataloging", label="Data Cataloging\n(Apache Atlas, Collibra)")
uml_diagram.add_node("DataQuality", label="Data Quality Management")
uml_diagram.add_node("DataSecurity", label="Data Security and Compliance")
uml_diagram.add_node("DataLineage", label="Data Lineage")
uml_diagram.add_node("MDM", label="Master Data Management")
uml_diagram.add_node("GovPlatform", label="Governance Platform")
uml_diagram.add_node("GovMonitoring", label="Monitoring and Reporting")

uml_diagram.add_node("MediaServer", label="Media Server\n(Jellyfin, FFmpeg)")
uml_diagram.add_node("BackupSystem", label="Backup System\n(Nextcloud, ZFS/Btrfs)")

uml_diagram.add_node("AIMessaging", label="AI-Powered Messaging")
uml_diagram.add_node("CalendarManagement", label="Calendar Management")
uml_diagram.add_node("DataLakes", label="Data Lakes and Warehousing")
uml_diagram.add_node("CRMIntegration", label="CRM Integration")
uml_diagram.add_node("ProjectManagement", label="Project Management")
uml_diagram.add_node("AIDashboard", label="AI Dashboard")
uml_diagram.add_node("EnhancedCompute", label="Enhanced Compute Power")

# Define relationships
uml_diagram.add_edge("Infrastructure", "OS")
uml_diagram.add_edge("Infrastructure", "Software")
uml_diagram.add_edge("Infrastructure", "DataAI")
uml_diagram.add_edge("Infrastructure", "Management")
uml_diagram.add_edge("Infrastructure", "Governance")
uml_diagram.add_edge("Infrastructure", "MediaBackup")
uml_diagram.add_edge("Infrastructure", "AIBusiness")

uml_diagram.add_edge("Software", "WebServers")
uml_diagram.add_edge("Software", "Databases")
uml_diagram.add_edge("Software", "Containers")

uml_diagram.add_edge("DataAI", "DataScience")
uml_diagram.add_edge("DataAI", "DataEngineering")
uml_diagram.add_edge("DataAI", "AIFrameworks")
uml_diagram.add_edge("DataAI", "ContinuousLearning")
uml_diagram.add_edge("DataAI", "DocGeneration")

uml_diagram.add_edge("Management", "Monitoring")
uml_diagram.add_edge("Management", "ConfigManagement")
uml_diagram.add_edge("Management", "BackupTools")

uml_diagram.add_edge("Governance", "DataGovFramework")
uml_diagram.add_edge("Governance", "DataCataloging")
uml_diagram.add_edge("Governance", "DataQuality")
uml_diagram.add_edge("Governance", "DataSecurity")
uml_diagram.add_edge("Governance", "DataLineage")
uml_diagram.add_edge("Governance", "MDM")
uml_diagram.add_edge("Governance", "GovPlatform")
uml_diagram.add_edge("Governance", "GovMonitoring")

uml_diagram.add_edge("MediaBackup", "MediaServer")
uml_diagram.add_edge("MediaBackup", "BackupSystem")

uml_diagram.add_edge("AIBusiness", "AIMessaging")
uml_diagram.add_edge("AIBusiness", "CalendarManagement")
uml_diagram.add_edge("AIBusiness", "DataLakes")
uml_diagram.add_edge("AIBusiness", "CRMIntegration")
uml_diagram.add_edge("AIBusiness", "ProjectManagement")
uml_diagram.add_edge("AIBusiness", "AIDashboard")
uml_diagram.add_edge("AIBusiness", "EnhancedCompute")

# Save the diagram as an image
uml_diagram.draw("comprehensive_infrastructure_uml_diagram.png", prog="dot", format="png")