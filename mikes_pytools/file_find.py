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
    def recursive_by_extension(ext:str,path:str) :
        """_summary_

        Args:
            ext (str): Extension not including '.'
            path (str): Path to root folder

        Returns:
            list: List of files
        """
        out = []

        files = glob.glob(os.path.join(path,"*"),recursive=True)
        for item in files :
            if os.path.isdir(item) :
                out += FileFind.recursive_by_extension(ext,item)
            elif os.path.splitext(item)[-1] == '.'+ext :
                out.append(item)
        return out
