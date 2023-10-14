def get_file_types():
    return {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ai', '.psd', '.svg', '.webp', '.ico', '.ps'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xlsx', '.key', '.odp', '.pps', '.pptx', '.ods', '.xls', 'xlsm', '.odt', '.rtf', '.tex', '.wpd'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.3g2', '.3gp', '.flv', '.h264', '.m4v', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.webm', '.wmv'],
        'Music': ['.mp3', '.wav', '.flac', '.aif', '.cda', '.mid', '.midi', '.mpa', '.ogg', '.wma', '.wpl'],
        'Archives': ['.zip', '.rar', '.7z', '.arj', '.deb', '.pkg', '.rpm', '.z'],
        'Disc&Media': ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
        'Database': ['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'],
        'Webpages': ['.htm', '.html', '.xhtml', '.cer', '.part', '.jsp', '.asp'],
        'System Files': ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.ini', '.msi', '.sys', '.tmp'],
        'Executables': ['.apk', '.bat', '.bin', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.wsf'],
        'Developer': ['.c', '.cgi', '.pl', '.cpp', '.py', '.java', '.sh', '.swift', '.vb', '.php', '.h', '.class', '.cs'],
        'Others': [],  # For unrecognized file types
    }
