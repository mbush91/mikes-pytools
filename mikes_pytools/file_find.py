"""Library for finding files
"""

import glob
import os

class FileFind :
    """Static method to find files in different ways

    Returns:
        None: N/A
    """

    @staticmethod
    def recursive_by_extension(ext:str,path:str,ignore=None) :
        """_summary_

        Args:
            ext (str): Extension not including '.'
            path (str): Path to root folder
            ignore (list): List of filenames to ignore
        Returns:
            list: List of files
        """
        out = []

        files = glob.glob(os.path.join(path,"*"),recursive=True)
        for item in files :
            if os.path.isdir(item) :
                out += FileFind.recursive_by_extension(ext,item,ignore=ignore)
            elif os.path.splitext(item)[-1] == '.'+ext :
                if ignore is not None :
                    if os.path.basename(item) not in ignore :
                        out.append(item)
                else :
                    out.append(item)
        return out


FileFind.recursive_by_extension('py','./',ignore=["test"])
