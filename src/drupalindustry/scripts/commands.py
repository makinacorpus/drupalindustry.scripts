"""Shell commands of the drupalindustry.scripts package."""

#import ConfigParser
from optparse import OptionParser
import os
import subprocess
import sys


class DrupalIndustryCommand(object):
    """Proxy to scripts in bin/."""
    def __init__(self, argv=[]):
        self.argv = argv
        self.config_file = None
    
    def __call__(self):
        """Main command callback."""
        self.configure()
        self.run_command(self.command)
    
    def configure(self):
        """Read configuration from arguments and/or configuration files"""
        parser = OptionParser()
        
        (options, args) = parser.parse_args(self.argv)
        
        if len(self.argv) == 1:
            raise Exception('Usage: %s COMMAND' % sys.argv[0])
        
        self.command = self.argv[1]

        # Detect paths
        self.project_dir = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(self.argv[0]))))
        self.commands_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin')

    def run_command(self, command):
        """Proxy to command."""
        command_path = os.path.join(self.commands_dir, '%s' % self.command)
        if not os.path.exists(command_path):
            raise Exception("Unknown command %s" % self.command)
        args = ['bash', command_path]
        args.append(self.project_dir)
        subprocess.call(args)


def main():
    command = DrupalIndustryCommand(sys.argv[:])
    command() 


if __name__ == "__main__":
    main()
