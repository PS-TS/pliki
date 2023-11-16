public class Book {
    public String title;
    public String author;
    public int numberOfPages;


    public Book(String title, String author, int numberOfPages){
        if(numberOfPages < 0){
            this.numberOfPages = 1;
        } else{
            this.numberOfPages = numberOfPages;
        }

        if(title.isEmpty() || title == null){
            this.title = "";
        } else if(author.isEmpty() || author == null){
            this.author = "";
        } else{
            this.title = title;
            this.author = author;
        }
    }

    @Override
    public String toString(){
        return "Book: " + title + " by " + author + ", Pages: " + numberOfPages;
    }


    public void equals(Book k2){
        System.out.println(this.author.equals(k2.author));
        System.out.println(this.title.equals(k2.title));
        System.out.println(this.numberOfPages == k2.numberOfPages);
    }
}
