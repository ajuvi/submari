using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MonitorSubmari
{
    public class Punt
    {
        private double x;
        private double y;

        public Punt(double x, double y)
        {
            this.x = x;
            this.y = y;
        }

        public double X { 
            get { return x; } 
            set { x = value; }
        }

        public double Y
        {
            get { return y; }
            set { y = value; }
        }
    }
}
