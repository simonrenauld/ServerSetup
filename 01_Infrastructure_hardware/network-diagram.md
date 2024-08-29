graph TD
Internet((Internet)) -->|WAN| Firewall[Firewall]
Firewall --> Router[Router]
Router --> Switch[Core Switch]

subgraph "Hetzner Server Infrastructure"
    direction TB
    UnraidServer[Unraid Server]
    WebServer[Web Servers<br/>Nginx, Apache]
    DatabaseServer[Databases<br/>MySQL, PostgreSQL, MongoDB]
    ContainerHost[Containers<br/>Docker, Kubernetes]
    AIServer[AI/ML Server<br/>TensorFlow, PyTorch, LLaMA]
    DataScienceServer[Data Science Server<br/>Jupyter, RStudio]
    BackupServer[Backup Server<br/>Nextcloud, Rsync]
    MediaServer[Media Server<br/>Jellyfin]
    MonitoringServer[Monitoring<br/>Prometheus, Grafana]
    
    subgraph "Data Governance"
        DataCatalog[Data Catalog<br/>Apache Atlas]
        DataQuality[Data Quality<br/>Great Expectations]
        DataSecurity[Data Security<br/>Apache Ranger]
        
        DataCatalog --> DataQuality
        DataQuality --> DataSecurity
        DataSecurity --> BackupServer
    end
    
    UnraidServer --> WebServer
    UnraidServer --> DatabaseServer
    UnraidServer --> ContainerHost
    UnraidServer --> AIServer
    UnraidServer --> DataScienceServer
    UnraidServer --> BackupServer
    UnraidServer --> MediaServer
    UnraidServer --> MonitoringServer
    UnraidServer --> DataCatalog
end

subgraph "Network Services"
    direction TB
    DHCP[DHCP Server]
    DNS[DNS Server]
    VPN[VPN Server<br/>WireGuard]
    
    DHCP --> DNS
    DNS --> VPN
    VPN --> DHCP
end

subgraph "End Devices"
    direction TB
    Workstations[Workstations]
    MobileDevices[Mobile Devices]
    IoTDevices[IoT Devices]
    
    Workstations --> MobileDevices
    Workstations --> IoTDevices
    MobileDevices --> IoTDevices
end

Switch --> UnraidServer
Switch --> DNS
Switch --> Workstations
Workstations --> Router
MobileDevices --> Router
IoTDevices --> Router
VPN --> Router

classDef server fill:#ffe066,stroke:#333,stroke-width:2px;
classDef network fill:#66b3ff,stroke:#333,stroke-width:2px;
classDef data fill:#99cc99,stroke:#333,stroke-width:2px;
classDef enddevices fill:#ff9966,stroke:#333,stroke-width:2px;

class UnraidServer,WebServer,DatabaseServer,ContainerHost,AIServer,DataScienceServer,BackupServer,MediaServer,MonitoringServer,DataCatalog,DataQuality,DataSecurity server;
class DHCP,DNS,VPN network;
class Workstations,MobileDevices,IoTDevices enddevices;
