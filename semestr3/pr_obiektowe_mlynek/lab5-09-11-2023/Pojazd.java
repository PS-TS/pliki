public class Pojazd {

    public void jedz(){
        System.out.println("Pojazd jedzie");
    }
}


class Samochod extends Pojazd{
    @Override
    public void jedz(){
        super.jedz();
        System.out.println(this.getClass());
    }
}