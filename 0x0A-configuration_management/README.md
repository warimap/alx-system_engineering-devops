# Configuration management
Project done during **Full Stack Software Engineering studies** at **ALX**. It aims to learn about server configuration management using **Puppet**.

## Technologies
* Scripts written in Bash 4.3.11(1)
* Tested on Ubuntu 14.04 LTS
* Puppet 3.8

## Files

| Filename | Description |
| -------- | ----------- |
| `0-create_a_file.pp` | Create a file in `/tmp` |
| `1-install_a_package.pp` | Install `puppet-lint` |
| `2-execute_a_command.pp` | Create a manifest that kills a process named `killmenow` |
# Configuration management

In this project, I started working with Puppet as a configuration management
tool. I practiced writing Puppet manifest files to create a file, install a
package, and execute a command.

## Tasks :page_with_curl:

* **0. Create a file**
  * [0-create_a_file.pp](./0-create_a_file.pp): Puppet manifest file that
  creates a file `school` in the `/tmp` directory.
    * File permissions: `0744`.
    * File group: `www-data`.
    * File owner: `www-data`.
    * File content: `I love Puppet`.

* **1. Install a package**
  * [1-install_a_package.pp](./1-install_a_package.pp): Puppet manifest file
  that install `flask` from pip3.

* **2. Execute a command**
  * [2-execute_a_command.pp](./2-execute_a_command.pp): Puppet manifest file
  that kills the process `killmenow`.

