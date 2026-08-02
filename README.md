# ☸️ Kubernetes For DevOps - Workspace

Welcome to the **Kubernetes For DevOps** repository! This is a centralized workspace containing production-ready Kubernetes manifests, practice labs, deployment configurations, and real-world DevOps integration projects.

---

## 📂 Repository Structure

This repository is organized into distinct project folders and practice modules:

```text
Kubernetes_For_Devops/
├── K8s_Vault_Sync_App/k8s/         # Azure Key Vault + Secrets Store CSI Driver integration
├── Joke_App/k8s/               # Kubernetes manifests for Joke App deployment
├── Message_Viewer_App/k8s/     # Kubernetes manifests for Message Viewer App
├── Simple_Practice_Manifest/  # Basic K8s resources (Pods, Deployments, Services, ConfigMaps)
└── Notes/                      # Learning notes, commands, and troubleshooting guides

```

---

## 🚀 Featured Projects & Modules

### 🔐 1. K8s Vault Sync App (`/K8s_Vault_Sync_App`)

* **Description:** Integration of Azure Key Vault with Kubernetes using Secrets Store CSI Driver.
* **Key Features:** Mounts secrets securely as volumes into pods without exposing sensitive credentials.
* **Main Files:** `secret-provider-class.yaml`, `azure-creds-secret.yaml`, `deployment.yaml`

### 🎭 2. Joke App (`/Joke_App/k8s`)

* **Description:** Kubernetes deployment manifests for a containerized web application.
* **Main Files:** Deployment & Service configurations.

### ✉️ 3. Message Viewer App (`/Message_Viewer_App/k8s`)

* **Description:** Kubernetes setups for message viewer microservice testing.

### 🛠️ 4. Simple Practice Manifests (`/Simple_Practice_Manifest`)

* **Description:** Fundamental Kubernetes manifests covering basic objects like Deployments, NodePort/ClusterIP Services, Namespaces, and Volumes.

---

## ⚙️ Prerequisites & Tools Used

To practice or apply the manifests in this repository, you will need:

* **Kubernetes Cluster:** KinD (Kubernetes in Docker), Minikube, or AKS/EKS/GKE
* **CLI Tools:** `kubectl`, `helm`, `docker`
* **Cloud Platform:** Azure (for Key Vault integration labs)

---

## 🛠️ How to Use These Manifests

1. **Clone this repository:**

```bash
git clone [https://github.com/sachinthokal/Kubernetes_For_Devops.git](https://github.com/sachinthokal/Kubernetes_For_Devops.git)
cd Kubernetes_For_Devops

```

1. **Navigate to the specific project directory:**

```bash
cd K8s_Vault_Sync_App/K8s

```

1. **Apply the manifests:**

```bash
kubectl apply -f .

```

---

## ✍️ Author & Maintenance

* **Maintained by:** Sachin Thokal
* **GitHub:** [@sachinthokal](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fsachinthokal)

---

*Happy Kubernetes Learning & Shipping! 🚀*

---
