using System.ComponentModel;

namespace dikstra_moze_zadziala
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

            graf.DodajWezel(1);
            graf.DodajWezel(2);
            graf.DodajWezel(3);
            graf.DodajWezel(4);
            graf.DodajWezel(5);
            graf.DodajWezel(6);

            graf.DodajKrawedz(1, 2, 1);
            graf.DodajKrawedz(1, 3, 4);
            graf.DodajKrawedz(2, 3, 2);
            graf.DodajKrawedz(2, 4, 5);
            graf.DodajKrawedz(3, 4, 1);
            graf.DodajKrawedz(3, 5, 2);
            graf.DodajKrawedz(3, 6, 5);


            int startowyWezel = 1;
            Dictionary<int, int> najkrotszeDrogi = graf.AlgorytmDijkstry(startowyWezel);

            string message = "Najkrótsze drogi od węzła " + startowyWezel + ":\n";
            foreach (var droga in najkrotszeDrogi)
            {
                message += "Do węzła " + droga.Key + " - Koszt: " + droga.Value + "\n";
            }

            MessageBox.Show(message, "Wyniki Dijkstry", MessageBoxButtons.OK, MessageBoxIcon.Information);

        }
    }

    class Element
    {
        public int Dystans;
        public int Poprzednik;
        public bool CzyByło;

        public Element()
        {
            Dystans = int.MaxValue;
            Poprzednik = -1;
            CzyByło = false;
        }
    }

    class Wezel
    {
        public int Id;
        public Dictionary<int, int> Sasiedzi;

        public Wezel(int id)
        {
            Id = id;
            Sasiedzi = new Dictionary<int, int>();
        }
    }

    class Graf
    {
        private Dictionary<int, Wezel> wezly;

        public Graf()
        {
            wezly = new Dictionary<int, Wezel>();
        }

        public void DodajWezel(int id)
        {
            if (!wezly.ContainsKey(id))
            {
                wezly.Add(id, new Wezel(id));
            }
        }

        public void DodajKrawedz(int wezelId1, int wezelId2, int waga)
        {
            if (wezly.ContainsKey(wezelId1) && wezly.ContainsKey(wezelId2))
            {
                wezly[wezelId1].Sasiedzi.Add(wezelId2, waga);
                wezly[wezelId2].Sasiedzi.Add(wezelId1, waga);
            }
        }

        public  Dictionary<int, int> AlgorytmDijkstry(int startowyWezel)
        {
            Dictionary<int, Element> wynik = new Dictionary<int, Element>();

            foreach (var wezelId in wezly.Keys)
            {
                wynik.Add(wezelId, new Element());
            }

            wynik[startowyWezel].Dystans = 0;

            for (int i = 0; i < wezly.Count; i++)
            {
                int aktualnyWezel = ZnajdzNajkrotszy(wynik);
                wynik[aktualnyWezel].CzyByło = true;

                foreach (var sasiad in wezly[aktualnyWezel].Sasiedzi)
                {
                    if (!wynik[sasiad.Key].CzyByło)
                    {
                        int nowyDystans = wynik[aktualnyWezel].Dystans + sasiad.Value;
                        if (nowyDystans < wynik[sasiad.Key].Dystans)
                        {
                            wynik[sasiad.Key].Dystans = nowyDystans;
                            wynik[sasiad.Key].Poprzednik = aktualnyWezel;
                        }
                    }
                }
            }

            return PobierzNajkrotszeDrogi(wynik);
        }

        private int ZnajdzNajkrotszy(Dictionary<int, Element> wynik)
        {
            int minDystans = int.MaxValue;
            int minWezel = -1;

            foreach (var wezel in wynik)
            {
                if (!wezel.Value.CzyByło && wezel.Value.Dystans < minDystans)
                {
                    minDystans = wezel.Value.Dystans;
                    minWezel = wezel.Key;
                }
            }

            return minWezel;
        }

        private Dictionary<int, int> PobierzNajkrotszeDrogi(Dictionary<int, Element> wynik)
        {
            Dictionary<int, int> najkrotszeDrogi = new Dictionary<int, int>();

            foreach (var wezel in wynik)
            {
                najkrotszeDrogi.Add(wezel.Key, wezel.Value.Dystans);
            }

            return najkrotszeDrogi;
        }
    }
}
