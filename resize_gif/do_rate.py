from PIL import Image


output_dir = "/mnt/e/SFA/Campaign A/do_rates/"
old_gif = Image.open(output_dir+"M1.gif")
nframe = old_gif.n_frames


contours = []
for iframe in range(nframe-1):
    print(iframe)
    old_gif.seek(iframe)
    title = old_gif.crop((700, 20, 1700, 100))
#     title.show()
    contour = old_gif.crop((1200, 105, 2300, 370))
    contour.paste(title.resize((375, 30)), (350, 11))
    contours.append(contour)
    # contour.show()

contours[0].save(output_dir+"new_m1.gif",
                 save_all=True,
                 append_images=contours[1:],
                 optimize=False,
                 loop=0,
                 duration=50,
                 compress_level=0,
                 quality=100,
                 )

contours[0].save(output_dir+"new_m2.gif",
                 save_all=True,
                 append_images=[contours[x]
                                for x in np.arange(0, nframe, 4)][1:],
                 optimize=False,
                 loop=0,
                 duration=60,
                 compress_level=0,
                 quality=100,
                 )

# blank = Image.new('RGB', (500, 40), color=(255, 255, 255))
# blank.show()
# contour.paste(blank, (150, 1))
