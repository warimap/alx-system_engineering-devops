# Apache 500 Error Fix with Puppet

This project contains a Puppet manifest to automate the fix for an Apache 500 Internal Server Error. The fix was identified using `strace` and then automated with Puppet.

## Usage

1. Run `sudo puppet apply 0-strace_is_your_friend.pp` to apply the fix.
2. Verify that Apache is now returning a 200 OK response with `curl -sI 127.0.0.1`.

## Requirements

- Ubuntu 14.04 LTS
- Puppet 2.1.1
- Apache2

