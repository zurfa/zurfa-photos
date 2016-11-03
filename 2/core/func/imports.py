import os



def get_imports(Dir=None):
    """Generates list of files in specified (default if not) directory with valid extensions"""
    valid = ['.jpg', '.jpeg', '.txt']
    if not Dir:
        # Did the user specify a directory?
        # self.lg.logger.error("Directory not specified or invalid")
        raise OSError
    else:
        try:
            Files = os.listdir(Dir)
        except OSError:
            # self.lg.logger.critical("Error opening directory, does it exist? %s" % Dir)
            # raise exp.DirectoryError(Dir)
            raise OSError
        else:
            file_paths = []
            Lf = len(Files)
            if Lf > 0:
                # Found files in directory
                # self.lg.logger.info("Searching for files in %s" % Dir)
                for File in Files:
                    ext = os.path.splitext(File)[1]
                    if ext in valid:
                        # File has a valid extension
                        file_paths.append(("%s%s" % (Dir, File)))
                    else:
                        # File does not have a valid extension
                        pass
                Lfp = len(file_paths)
                if Lfp > 0:
                    # Found atleast one valid file
                    # self.lg.logger.info("Found %s/%s files with valid extensions in %s" % (Lfp, Lf, Dir))
                    return file_paths
                else:
                    # Did not find any valid files
                    # self.lg.logger.error("Did not find any valid files in directory. %s" % Dir)
                    # raise exp.ValidFilesError(Dir)
                    raise OSError
            else:
                # Did not find files in directory
                # self.lg.logger.error("Did not find any files in directory. %s" % Dir)
                # raise exp.NullDirectoryError(Dir)
                raise OSError