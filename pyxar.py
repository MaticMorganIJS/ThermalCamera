{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "461fe4ba-67e2-41d8-9f03-21fb1aa820af",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# libraries\n",
    "\n",
    "import os\n",
    "from PIL import Image\n",
    "import shutil\n",
    "from IPython.display import clear_output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1e9875cd-f59a-4030-8bde-1cd8bdb00302",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The active directory is: C:\\Users\\Matic\\Documents\\1_služba\\termalna_kamera\\metal_pencil_test\n",
      "There are 200 pictures in the specified directory.\n"
     ]
    }
   ],
   "source": [
    "# change the active directory to the directory with your pictures, aquire a list of all the picture files\n",
    "# N.B.: all images should already be in the .png format, which can be chosen when exporting them from the Irbis 3 software\n",
    "# N.B.: active_directory has to be a string, so write it's name inside \" \"\n",
    "# N.B.: if you're rerouting the path more than 1 directory deep, you have to use the double \\\\ symbol instead of a single \\ when changing the directory\n",
    "\n",
    "active_directory = 'metal_pencil_test'\n",
    "\n",
    "###############################################################################################################################\n",
    "\n",
    "path = 'C:\\\\Users\\\\Matic\\\\Documents\\\\1_služba\\\\termalna_kamera\\\\' + active_directory + '\\\\'\n",
    "os.chdir(path)\n",
    "\n",
    "print('The active directory is: ' + os.getcwd())\n",
    "\n",
    "pictures = os.listdir()\n",
    "num_of_pics = len(pictures)\n",
    "print('There are ' + str(num_of_pics) + ' pictures in the specified directory.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6415a243-734a-42c7-bccc-4b6ab579b17a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The pictures have been copied, renamed, resized and reformated to .png.\n",
      "The active directory is now: C:\\Users\\Matic\\Documents\\1_služba\\termalna_kamera\\metal_pencil_test\\metal_pencil_test_adjusted\n"
     ]
    }
   ],
   "source": [
    "# Copy the picture files in a new directory named 'active_directory'_adjusted and rename them in the following way:\n",
    "# file_name#.png, where 'file_name' is a name you chose, and # is the consecutive number of the picture.\n",
    "# Also resizes the image from WxH to 2*W x 2*H to ensure both dimensions are an even number\n",
    "# which is required by some ffmpeg commands\n",
    "\n",
    "file_name = \"name_your_file\"\n",
    "\n",
    "###############################################################################################################################\n",
    "\n",
    "temp_image = Image.open(pictures[0])\n",
    "old_size = temp_image.size\n",
    "new_size = [size * 2 for size in old_size]\n",
    "size = str(new_size[0]) + ':' + str(new_size[1])\n",
    "temp_image.close()\n",
    "\n",
    "pic_format = pictures[0].split('.')[1]\n",
    "\n",
    "new_folder = active_directory + '_adjusted'\n",
    "new_path = path + new_folder\n",
    "\n",
    "if os.path.exists(new_path):\n",
    "    shutil.rmtree(new_path)\n",
    "os.makedirs(new_folder)    \n",
    "\n",
    "for i, img in enumerate(pictures):\n",
    "    \n",
    "    clear_output(wait=True)\n",
    "    if (i % 3 == 0):\n",
    "        print('\\\\')\n",
    "    elif (i % 3 == 1):\n",
    "        print('|')\n",
    "    elif (i % 4 == 2):\n",
    "        print('/')\n",
    "    else:\n",
    "        print('-')\n",
    "    \n",
    "    temp_img = Image.open(img)\n",
    "    temp_img.resize(new_size)\n",
    "    temp_name = file_name + \"{:03d}\".format(i)\n",
    "    os.chdir(new_path)\n",
    "    temp_img.save(temp_name + '.' + 'png', 'PNG')\n",
    "    temp_img.close()\n",
    "    os.chdir(path)\n",
    "    \n",
    "clear_output(wait=True)\n",
    "print('The pictures have been copied, renamed, resized.')\n",
    "os.chdir(new_path)\n",
    "print('The active directory is now: ' + os.getcwd())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "94660d6e-4afd-4d89-91e6-275b11f5e69d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Patience, the movie is being made...\n",
      "Your movie is ready.\n",
      "ffmpeg -framerate 20 -i name_your_file%03d.png -r 20 name.mp4\n"
     ]
    }
   ],
   "source": [
    "# execute the ffmpeg command inside powershell to create a video from pictures\n",
    "# Command shape reference: ffmpeg -f image2 -i test%d.jpg test.mov (https://ffmpeg.org/faq.html#How-do-I-encode-single-pictures-into-movies_003f)\n",
    "# choose the name of the movie file and what format you'd like the movie to be, the input framerate and the output framerate\n",
    "# N.B.: the input framerate should be the framerate with which you recorded the video. You can however speed the video up or slow it down\n",
    "# by chosing a larger/smaller framerate\n",
    "# N.B.: if the output framerate is larger than the input framerate, additional idential frames will be added. If the output\n",
    "# framerate is smaller than the input framerate, some frames will be dropped\n",
    "\n",
    "movie_name = 'name'\n",
    "movie_format = 'mp4'\n",
    "input_framerate = '20'\n",
    "output_framerate = '20'\n",
    "\n",
    "###############################################################################################################################\n",
    "\n",
    "print(\"Patience, the movie is being made...\")\n",
    "\n",
    "ps_command = 'ffmpeg -framerate ' + input_framerate + ' -i ' + file_name + '%03d.png ' + '-r ' + output_framerate + ' ' + movie_name + '.' + movie_format\n",
    "os.system(ps_command)\n",
    "\n",
    "print(\"Your movie is ready.\")\n",
    "\n",
    "print(ps_command) # for debugging purposes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5394449-13b5-431c-883a-d0691fe39a66",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86a72072-f269-4cfc-b248-8752056256bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bc2c995-739c-4e28-ba36-3cb4fc6fc161",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
