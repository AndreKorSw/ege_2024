# Игорь Владимирович хранит на компьютере картинки и видео различного разме ра. Он хочет поместить как можно больше картинок и видео на флеш-накопитель, объём которого равен К Кбайт, причём так, чтобы не менее чем половина его объ ёма была зарезервирована под видео. Определите максимальное количество фал дов (картинок и видео), которое Игорь Владимирович может сохранить на флеш- накопителе, и максимальный объём сохранённого видео. Максимальный размер кар тинки 50 Кбайт
#
# Входные данные
#
# Входные данные представлены в файле следующим образом. В перной строке за писаны два числа: М количество всех изображений и видео, К объем флеш- накопителя. В следующих № строках находятся значения объёмов картинок и пиво в Кбайтах


f = open("")
n, k = map(f.readline().split())
a = [int(f.readline()) for i in range(n)]
images = sorted([x for x in a if x <= 50])
videos = sorted([x for x in a if x > 50])
volume_videos = 0
i = 0
while volume_videos < k /2:
    volume_videos += videos[i]
    i+=1
print("last added video", i - 1)
print("volume for pics", k - volume_videos)

volume_total = volume_videos
for i in range(len(images)):
    if volume_total + images[i] <= k:
        volume_total += images[i]
        last_image = i
    else:
        break
print("last added pic", last_image)
print("left volume", k - volume_total)
#изображения закончились, продолжаем добавлять видосы

for i in range(3714, len(videos)):
    if volume_total + videos[i]<= k:
        volume_total += videos[i]
        last_viedo = i
    else:
        break
print("The last video", last_viedo)
print("left volume", k - volume_total)
# ищем видео побольше которое может поместиться
max_video = videos[4096]
volume_total -= max_video

for i in range(4097, len(videos)):
    if volume_total + videos[i] <= k:
        max_video = videos[i]
print(max_video)
print((volume_total +max_video, k ))
#все видео от 0 до 4905
#все картинки от 0 до 4356
print(4356 + 4905)