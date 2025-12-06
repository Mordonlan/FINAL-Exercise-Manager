output "load_balancer_dns" {
  description = "DNS name of the load balancer"
  value       = aws_lb.main.dns_name
}

output "master_public_ip" {
  description = "Public IP of Kubernetes master node"
  value       = aws_instance.k8s_nodes[0].public_ip
}

output "worker_public_ips" {
  description = "Public IPs of Kubernetes worker nodes"
  value = [
    aws_instance.k8s_nodes[1].public_ip,
    aws_instance.k8s_nodes[2].public_ip
  ]
}

output "master_private_ip" {
  description = "Private IP of Kubernetes master node"
  value       = aws_instance.k8s_nodes[0].private_ip
}

output "worker_private_ips" {
  description = "Private IPs of Kubernetes worker nodes"
  value = [
    aws_instance.k8s_nodes[1].private_ip,
    aws_instance.k8s_nodes[2].private_ip
  ]
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}