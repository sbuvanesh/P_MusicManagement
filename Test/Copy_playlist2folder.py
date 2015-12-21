import shutil, os, sys

if __name__ == '__main__':
    if len(sys.argv) == 3:
        plylist_path = sys.argv[1]
        dst_path = sys.argv[2]
        os.chdir(dst_path)
        plylist_dst_dir = plylist_path.split('/')[-1].replace('.m3u','')
        if not os.path.exists(plylist_dst_dir):
            os.mkdir(plylist_dst_dir)
        try:
            plylist = open(plylist_path,'r')
            for line in plylist.readlines():
                if line[0:4]!='#EXT':
                    song=line.replace('\n','')
                    try:
                        shutil.copy(song,plylist_dst_dir)
                    except IOError as e:
                        print('Cannot copy file: '+song)
                        continue
            print('Completed')
        except Exception as e:
            print(e)
    else:
        print('Script usage: <script> <playlist_path> <destination_path>')
