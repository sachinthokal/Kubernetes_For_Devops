# ☸️ Kubernetes for DevOps — Notes & Hands-on Guide

Welcome to the **Kubernetes for DevOps** repository! 🚀  
This repository serves as a personal knowledge base, hands-on lab guide, and quick reference sheet for learning and mastering **Kubernetes (K8s)** from a DevOps perspective.

---

## 📌 Repository Purpose

* 📖 **Concepts & Architecture:** Clear explanations of core K8s components.
* 🛠️ **Hands-on Labs:** Practical manifests, exercises, and real-world scenarios.
* 📝 **Cheat Sheets & Notes:** Quick commands, troubleshooting guides, and best practices.
* 🧪 **Local Testing:** Manifests ready to run on local clusters (Minikube, Kind, or K3s).

---

## 🗺️ Topics Covered / Learning Roadmap

* [x] **Kubernetes Architecture & Core Concepts** (Control Plane, Worker Nodes, etcd, Kubelet)
* [x] **Basic Workloads** (Pods, ReplicaSets, Deployments, DaemonSets, StatefulSets)
* [x] **Networking & Services** (ClusterIP, NodePort, LoadBalancer, Ingress, CNI basics)
* [x] **Configuration & Storage** (ConfigMaps, Secrets, PersistentVolumes, PVCs, StorageClasses)
* [x] **Application Health & Probes** (Liveness, Readiness, Startup Probes)
* [x] **Security & Access Control** (RBAC, ServiceAccounts, Network Policies)
* [x] **Resource Management** (Requests, Limits, ResourceQuotas, LimitRanges)
* [x] **Package Management** (Helm Basics & Chart Structure)
* [x] **Troubleshooting & Debugging** (Pod crashes, logs, events, networking issues)

---

## 📂 Repository Structure

```text
.
├── 01-architecture/         # Architecture notes and component breakdowns
├── 02-workloads/            # Pods, Deployments, Jobs, CronJobs manifests
├── 03-services-networking/  # Service types, Ingress, NetworkPolicies
├── 04-config-and-secrets/   # ConfigMaps and Secrets examples
├── 05-storage/              # PV, PVC, StorageClass hands-on
├── 06-rbac-security/        # Roles, RoleBindings, ServiceAccounts
├── 07-troubleshooting/      # Debugging scenarios, issue resolution notes
└── cheatsheets/             # kubectl command cheat sheets & quick tips

```

---

## ⚡ Quick Start / Local Lab Setup

To practice the manifests in this repo, set up a local cluster using any of the following:

### Using Minikube

```bash
minikube start --driver=docker
kubectl get nodes

```

### Using Kind (Kubernetes in Docker)

```bash
kind create cluster --name k8s-devops
kubectl cluster-info --context kind-k8s-devops

```

---

## 📋 Essential `kubectl` Cheat Sheet

### Cluster & Node Info

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl describe node <node-name>

```

### Pod & Deployment Management

```bash
# Get all running pods with namespaces
kubectl get pods -A

# Create a deployment
kubectl create deployment my-app --image=nginx --replicas=3

# Scale a deployment
kubectl scale deployment my-app --replicas=5

# Rollout status & history
kubectl rollout status deployment/my-app
kubectl rollout history deployment/my-app
kubectl rollout undo deployment/my-app

```

### Troubleshooting & Logs

```bash
# Check pod events & status details
kubectl describe pod <pod-name>

# View real-time logs
kubectl logs -f <pod-name>
kubectl logs -f <pod-name> -c <container-name> # for multi-container pods

# Execute command inside a pod
kubectl exec -it <pod-name> -- /bin/sh

```

---

## 🔗 Related Repositories

* **GitOps & Production Manifests:** [argocd-for-devops](https://github.com/sachinthokal/argocd-for-devops) — Automated deployments and environment overlays via ArgoCD.

---

## ✍️ Author & Notes

Maintained by **Sachin Thokal** as a continuous learning reference for DevOps and Cloud Engineering. Feel free to star ⭐ the repo if you find these notes helpful!

---
