import java.time.LocalDateTime; // import the LocalDate class
import java.time.format.DateTimeFormatter;
class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        
        String str = "2023-01-01 " + event1[0];
        LocalDateTime dateTime10 = LocalDateTime.parse(str, formatter);

        str = "2023-01-01 " + event1[1];
        LocalDateTime dateTime11 = LocalDateTime.parse(str, formatter);

        str = "2023-01-01 " + event2[0];
        LocalDateTime dateTime20 = LocalDateTime.parse(str, formatter);

        str = "2023-01-01 " + event2[1];
        LocalDateTime dateTime21 = LocalDateTime.parse(str, formatter);

        
        
        
        if(dateTime11.isEqual(dateTime20)){
            System.out.println("equals");
            System.out.println(dateTime11.isEqual(dateTime20));

            System.out.println(dateTime11);
            System.out.println(dateTime20);
            return true;
        }
            System.out.println("not equals");

        if(dateTime21.isBefore(dateTime10)){
            return !dateTime21.isBefore(dateTime10);
        }
        return !dateTime11.isBefore(dateTime20);
        
        // if(dateTime11.isBefore(dateTime20) && dateTime10.isAfter(dateTime21)){
        //     return false;
        // }
        // else{
        //     return true;
        // }
    }
}