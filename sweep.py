import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


ext_mapping = {
    'document': [
        'doc', 'docx', 'log',
        'msg', 'odt', 'pages',
        'rtf', 'tex', 'txt',
        'wpd', 'wps',
    ],
    'dataFiles': [
        'csv', 'dat', 'ged',
        'key', 'keychain', 'ppt',
        'pptx', 'sdf', 'tar',
        'tax2016', 'tax2020', 'vcf',
        'xml',
    ],
    'audio': [
        'aif', 'iff', 'm3u', 'm4a',
        'mid', 'mp3', 'mpa', 'wav',
        'wma',
    ],
    'video': [
        '3g2', '3gp', 'asf', 'asf',
        'avi', 'flv', 'm4v', 'mov',
        'mp4', 'mpg', 'rm', 'srt',
        'swf', 'vob', 'wmv',
    ],
    '3dmodel': [
        '3dm', '3ds', 'max', 'obj',
    ],
    'image': [
        'bmp', 'dds', 'gif', 'heic',
        'jpg', 'png', 'psd', 'pspimage',
        'tga', 'thm', 'tif', 'tiff',
        'yuv',
    ],
    'vector': [
        'ai', 'eps', 'svg',
    ],
    'ebooks': [
        'pct', 'pdf', 'epub', 'mobi'
        'cbr',
    ],
    'spreadDoc': [
        'xlr', 'xls', 'xlsx',
    ],
    'database': [
        'accdb', 'db', 'dbf', 'mdb',
        'pdb', 'sql',
    ],
    'executable': [
        'apk', 'app', 'bat', 'cgi',
        'com', 'exe', 'gadget', 'jar',
        'wsf', 'ps1',
    ],
    'cad': [
        'dwg', 'dxf',
    ],
    'webfiles': [
        'asp', 'aspx', 'cer', 'cfm',
        'crdownload', 'csr', 'css', 'dcr',
        'htm', 'html', 'js', 'jsp',
        'php', 'rss', 'xhtml',
    ],
    'fonts': [
        'fnt', 'fon', 'otf', 'ttf',
    ],
    'sysfiles': [
        'cab', 'cpl', 'cur', 'deskthemepack',
        'dll', 'dmp', 'drv', 'icns',
        'ico', 'sys',
    ],
    'settingsfile': [
        'cfg', 'ini', 'prf',
    ],
    'encodedfiles': [
        'hqx', 'mim', 'uue',
    ],
    'archive': [
        '7z', 'deb', 'pkg', 'gz',
        'rar', 'rpm', 'sitx', 'tar.gz',
        'zip', 'zipx',
    ],
    'diskImage': [
        'bin', 'cue', 'dmg', 'iso',
        'mdf', 'toast', 'vcd',
    ],
    'code': [
        'c', 'class', 'cpp', 'cs',
        'dtd', 'fla', 'h', 'java',
        'lua', 'm', 'pl', 'py',
        'sh', 'sln', 'swift', 'vb',
        'vb', 'vcxproj', 'xcodeproj', 'kt',
        'ino', 'dart',
    ],
    'backup': [
        'bak', 'tmp',
    ],
    'misc': [
        'ics', 'msi', 'part', 'torrent',
    ],
}


class Monitor(FileSystemEventHandler):
    def __init__(self, folder):
        self._folder = str(folder)
        print(self._folder)
        if not self.dir_exist(self._folder):
            os.mkdir(self._folder)
    
    def on_any_event(self, event):
        for entry in os.listdir(path):
            if os.path.isfile(entry):
                exts = entry.split(".")[1]
                for item in ext_mapping:
                    if exts in ext_mapping[item]:
                        folder = os.path.join(self._folder, item)
                        if self.dir_exist(folder):
                            self.move_file(entry, folder)
                        else:
                            os.mkdir(folder)
                            self.move_file(entry, folder)
                    else:
                        pass
                    break
            elif os.path.isdir(entry):
                if entry != self._folder:
                    folder = os.path.join(self._folder, 'folders')
                    if self.dir_exist(folder):
                        self.move_file(entry, folder)
                    else:
                        os.mkdir(folder)
                        self.move_file(entry, folder)



    
    def dir_exist(self, folder):
        return os.path.exists(folder)

    def move_file(self, filename, folder):
        date = datetime.datetime.utcnow()
        sub_folder = os.path.join(folder, f"{date.year}-{date.month}-{date.day}")
        orignal_path = os.path.join(path, filename)
        dst_path = os.path.join(sub_folder, filename)
        if self.dir_exist(sub_folder):
            try:
                os.rename(orignal_path, dst_path)
            except:
                pass
        else:
            os.mkdir(sub_folder)
            try:
                os.rename(orignal_path, dst_path)
            except:
                pass


if __name__ == "__main__":
    os.chdir('C:\\Users\\user\\desktop')
    path = os.getcwd()
    go_recursively = True
    observer = Observer()
    events = Monitor(".\\eazyCoder")
    observer.schedule(events, path, recursive=go_recursively)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()