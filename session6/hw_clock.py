loop_count = 0
while loop_count <10:
    import datetime
    print("hiện tại bây giờ là",datetime.datetime.now())
    loop_count +=1
    if loop_count >=10:
        print("Đã đến giờ dậy rồi")   
        break
    
import pyglet

music = pyglet.resource.media('music.mp3')
music.play()

pyglet.app.run()