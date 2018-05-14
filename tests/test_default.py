import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# def test_docker_is_installed(Command, SystemInfo):
#     result = Command('docker version').stdout
#     if SystemInfo.hostname == 'ansible-role-docker-ce':
#         assert '17.03.0-ce' in result
#     if SystemInfo.hostname == 'ansible-role-docker-cs':
#         assert '1.13.1-cs3' in result


def test_docker_running_and_enabled(Service):
    docker = Service("docker")
    assert docker.is_running
    assert docker.is_enabled


def test_docker_daemon_file(File):
    f = File("/etc/docker/daemon.json")

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
