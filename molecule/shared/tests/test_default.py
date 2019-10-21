import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

logstash_id = "logstash"


def test_logstash_packages(host):
    pkg = host.package(logstash_id)
    assert pkg.is_installed


def test_logstash_is_running(host):
    svc = host.service(logstash_id)
    assert svc.is_running
    assert svc.is_enabled
    assert host.socket("tcp://0.0.0.0:5044").is_listening
    assert host.socket("tcp://::ffff:127.0.0.1:9600").is_listening


def test_logstash_user_exists(host):
    user = host.user(logstash_id)
    grp = host.group(logstash_id)
    assert logstash_id in user.groups
    assert user.exists
    assert grp.exists


def test_logstash_config_files(host):
    config_files = ['/etc/logstash/logstash.yml',
                    '/etc/logstash/log4j2.properties',
                    '/etc/logstash/conf.d/50_logstash-output.conf'
                    ]
    for cfg in config_files:
        assert host.file(cfg).is_file
