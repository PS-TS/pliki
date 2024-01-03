using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace kruskal
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            Graf graf = new Graf();

            Wezel5 n1 = new Wezel5(1);
            Wezel5 n2 = new Wezel5(2);
            Wezel5 n3 = new Wezel5(3);

            graf.listawierzcholkow.Add(n1);
            graf.listawierzcholkow.Add(n2);
            graf.listawierzcholkow.Add(n3);

            Krawedz k1 = new Krawedz(n1, n2, 5);
            Krawedz k2 = new Krawedz(n1, n2, 10);
            Krawedz k3 = new Krawedz(n3, n2, 15);
            Krawedz k4 = new Krawedz(n3, n2, 5);
            Krawedz k5 = new Krawedz(n1, n3, 2);
            
            graf.Add(k1);
            graf.Add(k2);
            graf.Add(k3);
            graf.Add(k4);
            graf.Add(k5);

            Graf minimalneDrzewo = graf.Kruskal();

            MessageBox.Show("Krawędzie minimalnego drzewa rozpinającego:");
            foreach (var krawedz in minimalneDrzewo.listakrawedzi)
            {
                MessageBox.Show($"{krawedz.wierzcholek1} -- {krawedz.wierzcholek2} : {krawedz.wartosc}");
            }
        }

        class Wezel5
        {
           int wartosc;
            List<Krawedz> listakrawedzi;
    
            public Wezel5(int wartosc)
            {
                this.wartosc = wartosc;
                this.listakrawedzi = new List<Krawedz>();
            }
        }

        class Krawedz
        {
            public Wezel5 wierzcholek1;
            public Wezel5 wierzcholek2;
            public int wartosc;

            public Krawedz(Wezel5 wierzcholek1, Wezel5 wierzcholek2, int wartosc)
            {
                this.wierzcholek1 = wierzcholek1;
                this.wierzcholek2 = wierzcholek2;
                this.wartosc = wartosc;
            }
        }

    class Graf
    {
        public List<Wezel5> listawierzcholkow;
        public List<Krawedz> listakrawedzi;

        public Graf()
        {
            this.listawierzcholkow = new List<Wezel5>();
            this.listakrawedzi = new List<Krawedz>();
        }

        public Graf(Krawedz k) : this()
        {
            this.listakrawedzi.Add(k);
            this.listawierzcholkow.Add(k.wierzcholek1);
            this.listawierzcholkow.Add(k.wierzcholek2);
        }

        int sprawdz(Krawedz k)
        {
            int liczba = 0;
            if (!this.listawierzcholkow.Contains(k.wierzcholek1))
                liczba++;
            if (!this.listawierzcholkow.Contains(k.wierzcholek2))
                liczba++;
            return liczba;
        }
    
            public void Add(Krawedz k)
            {
                this.listakrawedzi.Add(k);
                if (!this.listawierzcholkow.Contains(k.wierzcholek1))
                    this.listawierzcholkow.Add(k.wierzcholek1);
                if (!this.listawierzcholkow.Contains(k.wierzcholek2))
                    this.listawierzcholkow.Add(k.wierzcholek2);
            }
    
            public void Join(Graf g)
            {
                this.listawierzcholkow.AddRange(g.listawierzcholkow);
                this.listakrawedzi.AddRange(g.listakrawedzi);
            }

            public Graf Kruskal()
            {
                var krawedzie = this.listakrawedzi.OrderBy(k => k.wartosc);
                List<Graf> listagrafow = new List<Graf>();
    
                foreach (var krawedz in krawedzie)
                {
                    if (listagrafow.Count == 0)
                    {
                        listagrafow.Add(new Graf(krawedz));
                        continue;
                    }
                    
                    Graf czyponownie = null;
    
                    for (int i = 0; i < listagrafow.Count; i++)
                    {
                        var g = listagrafow[i];
                        var ile = g.sprawdz(krawedz);
    
                        if (ile == 0)
                        {
                            goto skok;
                        }
                        else if (ile == 1)
                        {
                            if (czyponownie == null)
                            {
                                g.Add(krawedz);
                                czyponownie = g;
                            }
                            else
                            {
                                czyponownie.Join(g);
                                listagrafow.RemoveAt(i);
                                break;
                            }
                        }
                    }
                    skok:;
                }
                return listagrafow.FirstOrDefault();
            }
        }
    }
}
