class TravelAgencies{
    private int regNo;
    private String agencyName;
    private String packageType;
    private int price;
    private boolean flightFacility;

    int getregNo(){
        return this.regNo;
    }
    void setregNo(int rno){
        this.regNo = rno;
    }
    String getagencyName(){
        return this.agencyName;
    }
    void setagencyName(String agencyName){
        this.agencyName = agencyName;
    }
    String getpackageType(){
        return this.packageType;
    }
    void setpackageType(String packageType){
        this.packageType = packageType;
    }
    int getprice(){
        return this.price;
    }
    void setprice(String price){
        this.price = price;
    }
    boolean getflightFacility(){
        return this.flightFacility;
    }
    void setprice(boolean flightFacility){
        this.flightFacility = flightFacility;
    }
    TravelAgencies(int regNo,String agencyName,String packageType,int price,boolean flightFacility){
        this.regNo = regNo;
        this.agencyName = agencyName;
        this.packageType = packageType; 
        this.price= price;
        this.flightFacility = flightFacility;      
    }
}
class Solution{
    static int findAgencyWithHighestPackagePrice(TravelAgencies[] arr){
        int max =0;
        for(TravelAgencies agency : arr){
            if(agency.getprice()>max){
                max = agency.getprice();
            }
        }
        return max;
    }
    static TravelAgencies agencyDetailsForGivenldAndType(TravelAgencies[] arr,int regNo,String packageType){
        for(TravelAgencies agency : arr){
            if(agency.getflightFacility() && agency.getregNo()== regNo && agency.getpackageType().equalsIgnoreCase(packageType)){
                return agency;
            }
        }
        return null;
    }
    public static void main(String[] args) {
        
    }
}