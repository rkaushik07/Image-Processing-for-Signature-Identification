class Program
    {
        static void Main(string[] args)
        {
            String path = @"D:\pdf\reg";
            int fCount = Directory.GetFiles(path, "*", SearchOption.AllDirectories).Length;
            for (int i = 1; i <= fCount; i++)
            {
                string text = System.IO.File.ReadAllText(@"D:\pdf\reg\Region" + i+".txt");
                String[] txt = text.Split(' ');
                var image = new Bitmap(@"D:\pdf\sample.png");
                int x = Convert.ToInt32(txt[0]);
                int y = Convert.ToInt32(txt[1]);
                int w = Convert.ToInt32(txt[2]);
                int h = Convert.ToInt32(txt[3]);
                Bitmap bmp = CropImage(image, x, y, w, h);
                bmp.Save(@"D:\pdf\crp\crop" + i+".png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
        public static Bitmap CropImage(Image source, int x, int y, int width, int height)
        {
            Rectangle crop = new Rectangle(x, y, width, height);

            var bmp = new Bitmap(crop.Width, crop.Height);
            using (var gr = Graphics.FromImage(bmp))
            {
                gr.DrawImage(source, new Rectangle(0, 0, bmp.Width, bmp.Height), crop, GraphicsUnit.Pixel);
            }
            return bmp;
        }
    }
