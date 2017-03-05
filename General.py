import os

# Makes a directory in a seperate folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project: " + directory)
        os.makedirs(directory)

# Create queue and crawl files
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawledMatches.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Creates a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data onto a new file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

    file.close()

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and put the items in a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Convert a set to a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)




















