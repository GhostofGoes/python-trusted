Suspicious modules and methods that should be included in the analysis.


## SCRATCHPAD
MOVE THESE ELSEWHERE


Global "weights" dict?


Glossary of terms?
* "directory space": the main directories the package starts and does its
"normal" work in. command line arguments, temporary files, the directory
the package was invoked in, etc.
* "trust": the level to which you expect the application to be well-behaved
and perform the stated operations correctly. Breaking trust includes not
only malicious operations, such as backdoors and data exfil, but also
bugs and poor programming practices, such as side effects, excessive
resource usage, hidden/undocumented features, and security vulnerabilities.



# Modules

## Special interest
* `winreg`: Windows Registry access
* `socket`: Low-level network operations
* `ctypes`:  foreign function library. Allows calling functions in DLLs
or shared libraries, which is a indicator of malware depending on the
DLL/SO being accessed and other indicators.
* `subprocess`:

### sqlite
`sqlite3`: Accessing sqlite3 database files. sqlite3 is a very common
file database format used by Firefox, Skype, and other widely used
programs. They often contain sensitive data, such as histories, user
information, and logs. Any access to them is therefore of special interest.

There are several heuristics that could be applied here
* If the db is outside of the package's directory space
* If the db is on a "sensitive list" of names and/or directories (e.g. Skype's db)
* If the db is in the directory space of a different application or
other sensitive direcotry space, e.g program files, /etc, and the like.

## Other
* Filesystem: `pathlib`, `glob`, `shutil`, `stat`, `filecmp`, `shelve`,
`dbm`, `pickle`
* Unusual filesystem access methods: `ntpath`, `posixpath`, `macpath`


# Methods
Methods that will factor into the analysis somehow.


## Filesystem
| Method   | Module   | Purpose       | Class      | Risks       | Related methods |
| -------- | -------- | ------------- | ---------- | ----------- | --------------- |
| `open`   | builtins | Reading files | Read/Write | File access | N/A |
| `chdir`  | `os` | Changing directories | Read | File access | `fchdir` |
| `getcwd` | `os` | Get current directory | Read | Information gathering | `getcwdb` |
| `access` | `os` | Use the real uid/gid to test for access to path | Read | Information gathering | N/A |




## Read: Information access
* OS environment
    * `os.environ`: Reads system environment variables, which is a common
      method of accessing API keys and other sensitive information.
      (Also: `os.environb`, `os.getenv()`, `os.getenvb()`)

### Filesystem
* `os.listdir()`: List contents of directory (Also: `os.scandir()`)
* `os.fdopen()`: gets the file object associated with a specific file
descriptor.Could be used to read information about other applications if
the package has the proper permissions. Combined with `os.read()`.

### Profiling/fingerprinting
* `os.get_terminal_size()`: Return the size of the terminal window
* `os.uname()`: Returns information identifying the current operating system.
Often used by malware to fingerprint the system for targetted attacks,
or to send to the C&C server.


## Write: modifying system somehow, changing values
* `os.exec*()` family of functions. Execute a new program that replaces
the current process. Unusual and usually indicitive of loading malware.
* Other process open methods: `os.popen()`, `os.system()`,
`os.spawn*()` family, `os.startfile()`
* `os.kill()`: Kill a process. Denial of service.
* `os.putenv()`: Modify environment (only applies to current process and
any processes spawned by it, so this is benign if it's not being read
anywhere else, and there are no processes being spawned. The same applies
for `os.unsetenv()` as well.
* `os.closerange()`: Close a range of file descriptors, ignoring errors.
Potential denial of service attack on another application.

### Filesystem
* `os.remove()`: Delete a file (Also: `os.rmdir()`)
* `os.chmod()`: Change file permission flags
* `os.chown()`: Change file owner/group
* `os.link()`: Create a hard link
* `os.rename()` Rename file or directory (Also: `os.renames()` and `os.replace()`)
* `os.mkdir()`: Create a directory (Also: `os.makedirs()`)

### Unix
* `os.setegid()`: Set processes' effective group ID (impersonation for elevation/permissions)
* `os.geteuid()`: Set processes' effective user ID (impersonation for elevation/permissions)
* `os.setgid()`: Set the group ID of the process (elevation/permissions)
* `os.setuid()`: Set the user ID of the process (elevation/permissions)
* `os.setpgid()`: Modify the Group ID of a specific process
* ...various other group/user ID methods for Unix


