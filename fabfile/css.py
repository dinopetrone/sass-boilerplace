from fabric.api import local, cd, get, env, roles, execute, task
from fabric.colors import green
from glob import iglob
from os import path


# paths
base_path           = "resources/css"
scss_path   = base_path + "/src"
css_path    = base_path + "/"
scss_format = base_path + "/src/{}.scss"
css_format  = base_path + "/{}.css"

#regx
match_scss = "{}/[a-zA-Z]*.scss"

# sass run execs
exec_sass_watch   = "sass -l --watch {}:{}"
exec_sass_compile = "sass --force --style compressed {} {}"


@task
def watch():
    """
    start a scss "watch" process on the src files
    """
    local(exec_sass_watch.format(scss_path, css_path))


@task
def compile():
    """
    compile desktop scss -> css; returns an array of css file paths
    """

    print(green("\n[CSS] Compiling Desktop CSS\n", bold=True))

    file_glob = iglob(match_scss.format(scss_path))
    css_file_list = []

    for i in file_glob:
        file_name = path.basename(i)
        file_name = path.splitext(file_name)[0]
        scss_file = scss_format.format(file_name)
        css_file  = css_format.format(file_name)

        local(exec_sass_compile.format(scss_file, css_file))
        css_file_list.append(css_file)

    return css_file_list


@task
def list():
    """
    returns an array of desktop css file paths
    """

    print(green("\n[CSS] Getting Desktop CSS List\n", bold=True))

    file_glob = iglob(match_scss.format(scss_path))

    css_file_list = []

    for i in file_glob:
        file_name = path.basename(i)
        file_name = path.splitext(file_name)[0]
        css_file  = css_format.format(file_name)

        css_file_list.append(css_file)

    print css_file_list
    return css_file_list