#Python
from random import randint

class Track:
    
    def __init__(self,title=None):
        self.title = title  

    def __str__(self):
        return str(self.title)

class Playlist():
    
    def __init__(self):
        self.waiting = []
        self.song = ""
        self.repro = []
        self.status = ""
        
        
    def add(self, data):
        self.waiting.append(data)
        return f'The song "{data}" has been added'

    def delete(self, data):
        
        if type(data) == str:
            for song in self.waiting:
                if song.title == data:
                    print(f'The song "{data}" just be eliminated')
                    self.waiting.remove(song)
                else:
                    print('Error name')
        
        elif type(data) == int:
            if len(self.waiting) >= data - 1:
                print(f'The song {data} is equal to "{self.waiting[data - 1]}" and going to be removed')
                self.waiting.pop(data - 1)

            else:
                print(f'Index error')

        elif type(data) == float:
            print(f'Type error: Floats are not allowed')

        elif type(data) == bool:
            print(f'Type error: Boolean are not allowed')

        else:
            print(f'Type error')

    def reset(self):
        if len(self.repro) > 0:
            self.waiting.extend(self.repro)
            print('The playlist has been reset')
            self.repro.clear()
        else:
            print(f'First play a song')
    
    def start(self):
        
        if self.song == "" and self.status != "":
            self.song = self.status
            self.status = ""

        elif len(self.waiting) > 0 and self.song == "":
            self.song = self.waiting[0]
            self.waiting.pop(0)
            result = f'The song "{self.song}" just start'

        elif len(self.waiting) > 0 and self.song != "":
            result = f'The song "{self.song}" is playing'                
            
        elif len(self.waiting) == 0 and self.song != "":
            result = f'The song "{self.song}" is playing'

        else:
            result = f'No songs found in the Playlist'
            
        return result
    
    def pause(self):

        if self.song != "":
            self.status = self.song
            self.song = ""
            print(f'The song {self.status} has just been paused')

        elif self.song == "" and self.status != "":
            print(f'The song {self.status} is paused')

        elif self.song == "" and self.status == "":
            print(f'Any song selected')

    def next(self):
    
        if len(self.waiting) > 0:
            self.repro.append(self.song)
            self.song = self.waiting[0]
            self.waiting.pop(0)
            result = f'Now the song "{self.song}" is playing'

        elif len(self.waiting) > 0 and self.song == "":
            result = f"Please, first execute '.start()' after the playlist's name"

        elif len(self.waiting) == 0 and self.song == "" or self.song != "":
            result = f'The waiting list is empty'
        

        return result

    def previous(self):
        
        if len(self.repro) > 0:
            self.waiting.insert(0, self.song)
            self.repro.reverse()
            self.song = self.repro[0]
            self.repro.pop(0)
            self.repro.reverse()
            result = f'Now the song "{self.song}" is playing'

        else:
            if self.song != "":
                result = f'This is the first song on your playlist'
            else:
                result = f'Played songs list is empty'
        

        return result
    
    def playing(self):
    
        if self.song != "":
            result = f'The song "{self.song}" is playing'
        
        elif self.song == "" and self.status != "":
            result = f'The song {self.status} is paused'
        else:
            result = f'Any song is selected'

        return result

    def random(self):
        list_random = []
        if len(self.waiting) == 0:
            print(f'The playlist is empty')

        elif len(self.waiting) <= 2:
            print(f'You need more songs')

        else:
            while len(self.waiting) > 1:
                a = randint(0, len(self.waiting) -1)
                list_random.append(self.waiting[a])
                self.waiting.pop(a)
                
                if len(self.waiting) == 1:
                    list_random.append(self.waiting[0])
                    self.waiting.pop(0)

            self.waiting.extend(list_random)
            print(f'The random playlist has been created with {len(self.waiting)} songs')

    def reproduced(self):

        if len(self.repro) > 0:
            counter = 1
            for song in self.repro:
                
                print(f'{counter}.- {song}')
                counter += 1

        else:
            print('Any songs is here')

    def wait_songs(self):

        if len(self.waiting) > 0:
            counter = 1
            for song in self.waiting:

                print(f'{counter}.- {song}')
                counter += 1
        else:
            print('The playlist is empty')
            