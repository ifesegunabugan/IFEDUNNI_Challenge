# Repeated error when trying to run playbook:

Ifedunnis-MacBook-Air:~ IfedunniSegun-Abugan$ ansible-playbook play.yml
 [WARNING]: Unable to parse /etc/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] *******************************************************************************************************************************************************************************************

TASK [create a security group in us-east-2] ****************************************************************************************************************************************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: '  name: ec2 launcher\n'
fatal: [localhost]: FAILED! => {"changed": false, "module_stderr": "Traceback (most recent call last):\n  File \"/Users/IfedunniSegun-Abugan/.ansible/tmp/ansible-tmp-1557974915.43-96211777892458/AnsiballZ_ec2_group.py\", line 113, in <module>\n    _ansiballz_main()\n  File \"/Users/IfedunniSegun-Abugan/.ansible/tmp/ansible-tmp-1557974915.43-96211777892458/AnsiballZ_ec2_group.py\", line 105, in _ansiballz_main\n    invoke_module(zipped_mod, temp_path, ANSIBALLZ_PARAMS)\n  File \"/Users/IfedunniSegun-Abugan/.ansible/tmp/ansible-tmp-1557974915.43-96211777892458/AnsiballZ_ec2_group.py\", line 48, in invoke_module\n    imp.load_module('__main__', mod, module, MOD_DESC)\n  File \"/var/folders/xh/r0ly7vkd0sz447c42dhcvk340000gn/T/ansible_ec2_group_payload_o4GO5u/__main__.py\", line 299, in <module>\n  File \"/var/folders/xh/r0ly7vkd0sz447c42dhcvk340000gn/T/ansible_ec2_group_payload_o4GO5u/ansible_ec2_group_payload.zip/ansible/module_utils/aws/core.py\", line 69, in <module>\n  File \"/var/folders/xh/r0ly7vkd0sz447c42dhcvk340000gn/T/ansible_ec2_group_payload_o4GO5u/ansible_ec2_group_payload.zip/ansible/module_utils/ec2.py\", line 42, in <module>\n  File \"/Users/IfedunniSegun-Abugan/Library/Python/2.7/lib/python/site-packages/boto/__init__.py\", line 53, in <module>\n    config = Config()\n  File \"/Users/IfedunniSegun-Abugan/Library/Python/2.7/lib/python/site-packages/boto/pyami/config.py\", line 63, in __init__\n    self.read(BotoConfigLocations)\n  File \"/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ConfigParser.py\", line 305, in read\n    self._read(fp, filename)\n  File \"/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ConfigParser.py\", line 512, in _read\n    raise MissingSectionHeaderError(fpname, lineno, line)\nConfigParser.MissingSectionHeaderError: File contains no section headers.\nfile: /Users/IfedunniSegun-Abugan/.boto, line: 1\n'  name: ec2 launcher\\n'\n", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error", "rc": 1}
	to retry, use: --limit @/Users/IfedunniSegun-Abugan/play.retry

PLAY RECAP *************************************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1   

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next steps were to install tomcat server onto machine and then employ the index.html to bin files


