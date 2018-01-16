class Program
    {
        static void Main(string[] args)
        { String path = @"C:\SDA\SDA_Clean";
            int fCount = Directory.GetFiles(path, "*", SearchOption.AllDirectories).Length;
            for (int i = 1; i <= fCount; i++)
            {
                bool stat = IsBlank(@"C:\SDA\SDA_Clean\expsign"+i+".png");
                if (stat == true)
                {
                    File.Delete(@"C:\SDA\SDA_Clean\expsign"+i+".png");
                }
            }

        }
        public static bool IsBlank(string imageFileName)
        {
            double stdDev = GetStdDev(imageFileName);
            return stdDev < 100000;
        }

        public static double GetStdDev(string imageFileName)
        {
            double total = 0, totalVariance = 0;
            int count = 0;
            double stdDev = 0;

            // First get all the bytes
            using (Bitmap b = new Bitmap(imageFileName))
            {
                BitmapData bmData = b.LockBits(new Rectangle(0, 0, b.Width, b.Height), ImageLockMode.ReadOnly, b.PixelFormat);
                int stride = bmData.Stride;
                IntPtr Scan0 = bmData.Scan0;
                unsafe
                {
                    byte* p = (byte*)(void*)Scan0;
                    int nOffset = stride - b.Width * 3;
                    for (int y = 0; y < b.Height; ++y)
                    {
                        for (int x = 0; x < b.Width; ++x)
                        {
                            count++;

                            byte blue = p[0];
                            byte green = p[1];
                            byte red = p[2];

                            int pixelValue = Color.FromArgb(0, red, green, blue).ToArgb();
                            total += pixelValue;
                            double avg = total / count;
                            totalVariance += Math.Pow(pixelValue - avg, 2);
                            stdDev = Math.Sqrt(totalVariance / count);

                            p += 3;
                        }
                        p += nOffset;
                    }
                }

                b.UnlockBits(bmData);
            }

            return stdDev;
        }

    }
