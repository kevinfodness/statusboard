# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # Use the official Ubuntu xenial64 box as a base.
  config.vm.box = "debian/jessie64"

  # Create a private network, which allows host-only access to the machine using a specific IP.
  config.vm.network "private_network", ip: "192.168.56.110"

  # VirtualBox specific configuration.
  config.vm.provider "virtualbox" do |vb|
    vb.name = "statusboard-dev"
    vb.cpus = "1"
    vb.memory = "1024"
  end

  # Provisioning configuration. Tells Vagrant what script to run during the provisioning process.
  config.vm.provision :shell, path: "provision.sh"

  # Tell Vagrant to forward the X11 session.
  config.ssh.forward_x11 = true
end
