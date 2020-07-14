
import os
import time

ATARI_SECTOR_SIZE = 0x80
ATARI_NB_SECTORS = 0x2d0
ATARI_NB_SECTORS_DOUBLE = 0x410
ATARI_ERR_CANT_WRITE = "Can't write on disk!"
ATARI_ERR_BAD_SECTOR_SIZE = "Bad number of bytes in sector!"
ATARI_SINGLE_DENSITY_SIZE = ATARI_NB_SECTORS * ATARI_SECTOR_SIZE
ATARI_DOUBLE_DENSITY_SIZE = ATARI_NB_SECTORS_DOUBLE * ATARI_SECTOR_SIZE

class DISK():
    def __init__(self, fname=None, read_only=False):
        self.disk_name = None
        self.readonly_flag = None
        self.__read_sector_callback = None
        self.__write_sector_callback = None

    def setReadSectorCallback(self, hook):
        self.__read_sector_callback = hook

    def setWrittenSectorCallback(self, hook):
        self.__write_sector_callback = hook

    def insertDisk(self, disk_name, readonly_flag=0):
        self.disk_name = disk_name
        self.readonly_flag = readonly_flag

    def ejectDisk(self):
        self.disk_name = None
        self.readonly_flag = None

    def isEnhancedDensity(self):
        if not self.diskRemoved():
            with open(self.getFilename(), "rb") as fp:
                fp.seek(0, 2)
                size = fp.tell()
            if size >= ATARI_DOUBLE_DENSITY_SIZE:
                return 1
        return 0

    def getStatus(self):
        # http://atariage.com/forums/topic/220085-sio-command-getstatus-applied-to-disk-drive/#entry2892881
        # Bit which really matter are aux1 bits 5 and 7.
        # Some programs also look for aux4 bit 4
        # (this allows to detect floppy swapping automatically).
        aux1 = 0x10 + self.isEnhancedDensity() * 0x80
        aux2 = self.diskRemoved() + self.getReadonlyFlag() * 0x40 + self.diskRemoved() * 0x80
        return aux1, aux2

    def readSector(self, secnum):
        if not self.diskRemoved():
            if self.__read_sector_callback != None:
                self.__read_sector_callback(secnum)
            with open(self.getFilename(), 'rb') as fp:
                fp.seek((secnum-1) * ATARI_SECTOR_SIZE)
                cars = fp.read(ATARI_SECTOR_SIZE)
            return cars
        else:
            time.sleep(1.0)
            return None

    def writeSector(self, secnum, sector):
        if self.__write_sector_callback != None:
            self.__write_sector_callback(secnum)
        if self.getReadonlyFlag():
            return ATARI_ERR_CANT_WRITE
        if len(sector) != ATARI_SECTOR_SIZE:
            return ATARI_ERR_BAD_SECTOR_SIZE
        with open(self.getFilename(), 'rb+') as fp:
            fp.seek((secnum-1) * ATARI_SECTOR_SIZE)
            fp.write(sector)

    def formatDisk(self, nb_sectors, sector_size):
        with open(self.getFilename(), "wb") as fp:
            fp.write(chr(0) * nb_sectors * sector_size)

    def getReadonlyFlag(self):
        if self.readonly_flag:
            return 1
        else:
            return 0

    def setReadonlyFlag(self, value):
        if not value:
            self.readonly_flag = 0
        else:
            self.readonly_flag = 1

    def diskRemoved(self):
        if self.disk_name == None:
            return 1
        if os.path.isfile(self.disk_name):
            return 0
        else:
            return 1
        
    def getFilename(self):
        if self.diskRemoved():
            return None
        else:
           return self.disk_name

    def setFilename(self, filename):
        self.disk_name = filename

    def __str__(self):
        text = "<DISK> filename=%s read_only=%u disk_removed=%u"%(self.getFilename(), self.getReadonlyFlag(), self.diskRemoved())
        return text

if __name__ == "__main__":
    
    import Tkinter as tk
    
    def utest():
        # Test console mode
        disk = DISK()
        assert disk.getFilename() == None
        assert disk.getReadonlyFlag() == 0
        assert disk.diskRemoved() == 1
        disk = DISK()
        disk.insertDisk("utest/mandatory/FILEDISK")
        assert disk.getFilename() == "utest/mandatory/FILEDISK"
        assert disk.getReadonlyFlag() == 0
        assert disk.diskRemoved() == 0
        disk.setReadonlyFlag(1)
        assert disk.getReadonlyFlag() == 1
        assert disk.diskRemoved() == 0
        disk.setFilename("utest/mandatory/MYMAZE")
        assert disk.getFilename() == "utest/mandatory/MYMAZE"
        disk.setFilename("toto") # "toto" is not supposed to exist
        assert disk.getFilename() == None        
        assert disk.getReadonlyFlag() == 1
        assert disk.diskRemoved() == 1
        # test tkinter mode
        win = tk.Tk()
        disk = DISK()
        assert disk.getReadonlyFlag() == 0
        disk.read_only_var = tk.IntVar()
        assert disk.getReadonlyFlag() == 0
        disk.setReadonlyFlag(33)
        assert disk.getReadonlyFlag() == 1
        assert disk.diskRemoved() == 1
        disk.fname_var = tk.StringVar()
        assert disk.diskRemoved() == 1
        disk.fname_var.set("toto")
        assert disk.diskRemoved() == 1
        assert disk.getFilename() == None
        disk.setFilename("utest/mandatory/FILEDISK")
        assert disk.getFilename() == "utest/mandatory/FILEDISK"
        assert disk.diskRemoved() == 0
        # test getStatus
        disk.setReadonlyFlag(False)
        assert disk.getStatus() == (16, 0)
        disk.setReadonlyFlag(True)
        assert disk.getStatus() == (16, 64)
        #end of utest
        win = None
        print "A L L   T E S T S   P A S S E D !"

    utest()

    #~ import class_sio as SIO
    #~ sio = SIO.SIO()
    #~ sio.mountDrive("1", "utest/mandatory/MYMAZE")   
    #~ sio.mountDrive("1")
    #~ sio.open(port=3, timeout=1.0)
    #~ disk = sio.getDevice("1")
    #~ disk.fname = None
    #~ print sio
    #~ sio.sequencer
