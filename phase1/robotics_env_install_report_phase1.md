# Robotics Simulation Development Environment Install Report

Generated: 2026-07-09 09:24:00 +08:00

## Install Roots

- ToolRoot: `F:\robotics`
- DownloadRoot: `F:\robotics-install-cache`
- Log: `C:\Users\Administrator\Documents\Codex\2026-07-06\nis\install_logs\setup_20260709_092137.log`
- Note: D drive is not present; fallback roots were used: ToolRoot=F:\robotics, DownloadRoot=F:\robotics-install-cache.

## Component Status

| Component | State | Version/Output | Path | Validation | Notes |
| --- | --- | --- | --- | --- | --- |
| Install policy | VERIFY |  | F:\robotics | incremental install; no deletion; D fallback handled |  |
| Git | SKIP_INSTALLED | usage: git [-v / --version] [-h / --help] [-C <path>] [-c <name>=<value>]<br>           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]<br>           [-p / --paginate / -P / --no-pager] [--no-replace-objects] [--no-lazy-fetch]<br>           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]<br>           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>] | C:\Program Files\Git\cmd\git.exe | git --version ok |  |
| Python 3.12 | NEED_UPGRADE | Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32<br>Type "help", "copyright", "credits" or "license" for more information.<br>>>>  |  | Python exists but is not 3.12 |  |
| Python 3.12 | VERIFY | Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32<br>Type "help", "copyright", "credits" or "license" for more information.<br>>>>  | F:\robotics\Python312\python.exe | python --version after install, exit 0 |  |
| VS Code | START_INSTALL |  |  | installing official winget package |  |
| VS Code | VERIFY |  | F:\Microsoft VS Code\bin\code.cmd | code --version after install |  |
| CMake | START_INSTALL |  |  | installing official Kitware package |  |
| CMake | VERIFY |  |  | cmake --version after install |  |
| Visual Studio 2022 C++ workload | START_INSTALL | 17.14.36518.9 | C:\Program Files\Microsoft Visual Studio\2022\Community | modifying existing Visual Studio |  |
| Visual Studio 2022 C++ workload | VERIFY | exit 1618 | C:\Program Files\Microsoft Visual Studio\2022\Community | vswhere recheck required |  |
| Docker Desktop | SKIP_INSTALLED | Usage:  docker [OPTIONS] COMMAND<br>System.Management.Automation.RemoteException<br>A self-sufficient runtime for containers<br>System.Management.Automation.RemoteException<br>Common Commands: | C:\Program Files\Docker\Docker\resources\bin\docker.exe | docker --version ok |  |
| Docker user config ACL | NEED_REPAIR |  | C:\Users\Administrator\.docker | ACL repaired for current user |  |
| Docker daemon | VERIFY | Usage:  docker [OPTIONS] COMMAND<br>System.Management.Automation.RemoteException<br>A self-sufficient runtime for containers<br>System.Management.Automation.RemoteException<br>Common Commands: |  | docker info checked | Docker Desktop may need user session after WSL repair |
| Microsoft-Windows-Subsystem-Linux | SKIP_INSTALLED | Enabled |  | feature enabled |  |
| VirtualMachinePlatform | SKIP_INSTALLED | Enabled |  | feature enabled |  |
| Microsoft-Hyper-V-All | START_INSTALL | Disabled |  | enabling Windows feature |  |
| WSL default version | VERIFY | 2 |  | wsl --set-default-version 2 ok |  |
| WSL kernel | VERIFY |  |  | wsl --update executed |  |
| Reboot | NEED_REPAIR |  |  | Windows features or WSL installation require reboot; run again with -ContinueAfterReboot after reboot |  |

## Environment Variables

```
Machine PATH:
F:\robotics\Python312\Scripts\;F:\robotics\Python312\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files (x86)\Common Files\Intel\Shared Libraries\redist\intel64_win\compiler;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Bandizip\;F:\Git\cmd;C:\Program Files\Git\cmd;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Common Files\Autodesk Shared\;C:\Program Files\Microsoft SQL Server\120\Tools\Binn\;F:\robotics\Python312;F:\robotics\Python312\Scripts;C:\Program Files\CMake\bin

User PATH:
F:\Scripts\;F:\;C:\Users\Administrator\AppData\Local\Microsoft\WindowsApps;;F:\Microsoft VS Code\bin;F:\cursor\resources\app\bin;C:\Users\Administrator\.dotnet\tools;C:\Users\Administrator\AppData\Local\Programs\Ollama
```
