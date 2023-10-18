namespace lab1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int liczba = (int)numericUpDown1.Value;
            MessageBox.Show("Suma: " + fibonacci(liczba));
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }


        int fibonacci(int liczba)
        {
            if (liczba == 0)
            {
                return 0;
            }
            else if (liczba == 1)
            {
                return 1;
            }
            else
            {
                return fibonacci(liczba - 1) + fibonacci(liczba - 2);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}