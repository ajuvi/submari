using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Xml.Linq;

namespace MonitorSubmari
{
    /// <summary>
    /// Lógica de interacción para MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string nomSubmari = "ictineu";
        private string url = "http://localhost:5000/mesura/ictineu";

        public MainWindow()
        {
            InitializeComponent();

            System.Windows.Threading.DispatcherTimer dispatcherTimer = new System.Windows.Threading.DispatcherTimer();
            dispatcherTimer.Tick += dispatcherTimer_Tick;
            dispatcherTimer.Interval = TimeSpan.FromSeconds(0.2);
            dispatcherTimer.Start();

        }

        private void dispatcherTimer_Tick(object sender, EventArgs e)
        {
            txtNom.Text = nomSubmari;

            Punt punt = GetPunt();
            if(punt is null)
            {
                lbX.Text = "X: ?";
                lbY.Text = "Y: ?";
            } else
            {
                lbX.Text = "X: " + punt.X;
                lbY.Text = "Y: " + punt.Y;
            }

        }

        private void txtNom_TextChanged(object sender, TextChangedEventArgs e)
        {
            nomSubmari = txtNom.Text;
        }

        //Obtenir els punts del servidor web
        private Punt GetPunt()
        {
            return new Punt(10,10);
        }


    }
}
