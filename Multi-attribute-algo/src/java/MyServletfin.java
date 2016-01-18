/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */


import au.com.bytecode.opencsv.CSVParser;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.FileReader;
import java.util.Iterator;
import java.util.List;
import au.com.bytecode.opencsv.CSVReader;
import java.net.URL;

/**
 *
 * @author sreepradhanathirumalaiswami
 */
public class MyServletfin extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code> methods.
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
          CSVReader reader = new CSVReader(new FileReader("/Users/sreepradhanathirumalaiswami/Documents/wireless/project/wireless.csv"));
           List<String[]> li=reader.readAll();


        try {
            /* TODO output your page here
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet MyServlet</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet MyServlet at " + request.getContextPath () + "</h1>");
            out.println("</body>");
            out.println("</html>");
            */
        //out.println("<h2>HELLO WELCOME TO SERVLET CODING</h2>");
        out.println("<html>");
        out.println("<head>");
        //out.println("INSIDE MYSERVLET");

        //out.println("<h1>HIIIIII</h1>");
        System.out.println("BEFORE CLOSING HEAD");
        out.println("<title>Servlet</title>");
        out.println("<style>");

        //out.println("<body>");
        System.out.println("<h1>Servlet MyServlet at " + request.getContextPath () + "</h1>");
        //out.println("</body>");


        out.println("<title>Servlet Servlet</title>");
        out.println("<style>");
        out.println("table,th,td");
        out.println("{");
        out.println("border:1px solid black;");
        out.println("}");
        out.println("</style>");
        out.println("<h1 style=\"margin-bottom:0;\">Total number of services available is "+li.size()+"</h1></div>");
       ;
        out.println("</head>");
        out.println("<body style=\"color:black\" >");
        out.println( "<div id=\"container\" style=\"width:500px\">");
        out.println( "<div id=\"header\" style=\"background-color:#FFA500;\">");
        out.println( "<h1 style=\"margin-bottom:0;\">FINAL SORTED LIST OF WEBSERVICES BASED ON FUZZY LOGIC MULTI ATTRIBUTE ALGORITHM</h1></div>");
        //out.println("HIIIIIIIIIIIII");

        //out.println(name);
           out.println("</html>");
            // create Iterator reference
  Iterator<String[]>i1= li.iterator();
  Iterator<String[]>i2=li.iterator();
  Iterator<String[]>i3=li.iterator();
  // Iterate all values
 /*while(i1.hasNext()){

 String[] str=i1.next();

 System.out.print(" Values are ");
//out.println(str);
// for(int i=0;i<str.length;i++)
//{

  // out.println(" "+str[1]);

//}

            }
 */
 i1.next();
 int count2=0;
 //out.println(li[0]);
 int num=10;//top records to be displayed
 int no=li.size()-1;
  int count=0;
float quality[][]=new float[no][9];
String webservices[]=new String[no];
//out.println(" before countloop");
while(count<no)
{   //out.println(count);
    //out.println("Inside countloop");

    //out.println(count);
    String[] str=i1.next();
     //out.println(str);



    //out.println(count);
    for(int t=0;t<9;t++)
  {
    //out.println("QUALITY");
    //out.println(str[t]);
    quality[count][t]=Float.valueOf(str[t]);
    //out.println(quality[count][t]);
    }
    webservices[count]=str[10];
    count =count+1;
    //out.println("Count");
    //out.println(count);
}
//out.println("After quality initialization");
float temp[]=new float[40];
float maximum[]=new float[9];
float minimum[]=new float[9];
int cnt=0;
int i=0,j=0;
/*ResultSet rs = s
.executeQuery("select * from project.qos");

while (rs.next()) {
j=0;
float q1 = rs.getFloat("q1");
quality[i][j]=q1;
j++;
float q2 = rs.getFloat("q2");
quality[i][j]=q2;
j++;
float q3 = rs.getFloat("q3");
quality[i][j]=q3;
j++;
float q4 = rs.getFloat("q4");
quality[i][j]=q4;
j++;
float q5 = rs.getFloat("q5");
quality[i][j]=q5;
j++;
i++;
System.out.println("q1 " + q1);
System.out.println("q2 " + q2);
System.out.println("q3" + q3);
System.out.println("q4 " + q4);
System.out.println("q5" + q5);
}*/

float max=0;
//out.println("Bafore maxloop");
for( j=0;j<9;j++)
{


max=quality[0][j];

for( i=0;i<no;i++)
{
if(max<quality[i][j])
max=quality[i][j];
}
maximum[j]=max;
}
//out.println("Max");
//out.println(max);
float min=0;
for( j=0;j<9;j++)
{
min=quality[0][j];
for( i=0;i<no;i++)
{
if(quality[i][j]<min)
{
min=quality[i][j];
}
}
minimum[j]=min;
}
//out.println("Min");
//out.println(min);
float v[][]=new float[no][10];
for( i=0;i<no;i++)
{
for( j=0;j<9;j++)
{
    if(j==0)
v[i][j]=1-(quality[i][j]/(maximum[j]+minimum[j]));
    else  if(j==7)
       v[i][j]=1-(quality[i][j]/(maximum[j]+minimum[j]));
    else
v[i][j]=quality[i][j]/(maximum[j]+minimum[j]);
}
}
/*for(i=0;i<no;i++)
{ for( j=2;j<9;j++)
{
v[i][j]=quality[i][j]/(maximum[j]+minimum[j]);
}
}*/
for( i=0;i<no;i++)
{ for( j=0;j<9;j++)
{
//out.print(v[i][j]+"\t");
}
}
float g[]=new float[9];
String array[]=new String[9];
float min1;
float b[]=new float[9];
float max1;
for(j=0;j<9;j++)
{ min1=v[0][j];
for(i=0;i<no;i++)
{
if(v[i][j]<min1)
{
min1=v[i][j];
}
}
b[j]=min1;
}
for( j=0;j<9;j++)
{
max1=v[0][j];
for( i=0;i<no;i++)
{
if(v[i][j]>max1)
{max=v[i][j];}
}
g[j]=max1;
}
out.println("hiiii");
String restime=(String) request.getParameter("restime");
//request.setAttribute("restime", restime);
out.println(restime);
String availability=request.getParameter("availability");
request.setAttribute("availability", availability);
//String throughput=request.getParameter("throughput");
//request.setAttribute("throughput", throughput);
String success=request.getParameter("success");

out.println(success);
request.setAttribute("success", success);
String reliability=request.getParameter("reliability");
request.setAttribute("reliability", reliability);
String compliance=request.getParameter("compliance");
request.setAttribute("compliance", compliance);
String bestpractices=request.getParameter("bestpractices");
request.setAttribute("bestpractices", bestpractices);
String latency=request.getParameter("latency");
request.setAttribute("latency", latency);
//out.println("Availability");




/*float w[]=new float[9];
//w[0]=(float) 0.1;
w[0]=(Float.valueOf(restime)/(float)100);
w[1]=(float) 0.3;
w[2]=(float) 0.2;
w[3]=(float) 0.1;
w[4]=(float) 0.3;
 */
 

float w[]=new float[9];
w[0]=(Float.valueOf(restime)/(float)100);
w[1]=Float.valueOf(availability)/(float)100;
//w[2]=Float.valueOf(throughput)/(float)100;
w[2]=0;

w[3]=Float.valueOf(success)/(float)100;
//w[4]=Float.valueOf(reliability)/(float)100;
//w[5]=Float.valueOf(compliance)/(float)100;
//w[6]=Float.valueOf(bestpractices)/(float)100;
//w[7]=Float.valueOf(latency)/(float)100;
//w[8]=Float.valueOf(50/(float)100);
//w[9]=0.0;
i=0;j=0;
float wed[]=new float[no];
while(i<no)
{j=0;
while(j<9)
{
wed[i]=wed[i]+((w[j]*(g[j]-v[i][j]))*((w[j]*(g[j]-v[i][j]))));
j++;
}
wed[i]=(float) Math.pow(wed[i],0.5);
i++;
}
i=0;
float wed1[]=new float[no];
while(i<no)
{j=0;
while(j<9)
{
wed1[i]=wed1[i]+((w[j]*(v[i][j]-b[j]))*((w[j]*(v[i][j]-b[j]))));
j++;
}
wed1[i]=(float) Math.pow(wed1[i],0.5);
i++;
}
float fin[]=new float[no];
for(i=0;i<no;i++)
{
fin[i]=1/(1+((wed[i]/wed1[i])*(wed[i]/wed1[i])));
//out.println("FIN");
//out.println(""+fin[i]);
}
int order[]=new int[no];
float fin1[]=new float[no];
for(i=0;i<no;i++)
fin1[i]=fin[i];
float temp1;
for(i=0;i<no;i++)
{
for(j=i;j<no;j++)
{
if(fin[i]<fin[j])
{
temp1=fin[i];
fin[i]=fin[j];
fin[j]=temp1;
}
}
}
for(i=0;i<no;i++)
{
for(j=0;j<no;j++)
{
if(fin[i]==fin1[j])
{
    order[i] = j;

}
}
}
//out.println("Order");
for(i=1;i<num+1;i++)
{
   // out.println(order[i]);

            }
//out.println("FINAL VALUES");


   //out.println("The TOP 10 best services ");
out.println("<body bgcolor='azure' style='color:white' >");

out.println("<table style=\"width:300px\" border=\"2\" >");
//out.println("<tr>");

String[] attrs=i2.next();
for(int t=0;t<9;t++)
{

out.println("<td>");
out.println(attrs[t]);
out.println(" </td>");


}
//out.println(" </tr>");
//out.println(attrs[0]);
i2.next();
//while(count2<no)
//{
    //out.println("Count final");
    //out.println(count2);
    for(j=0;j<2500;j++)
    {
        //String[] str = i2.next();
Iterator<String[]>i4= li.iterator();
    for(i=1;i<250;i++)
{
String[] str = i4.next();
    if(i==order[j])
    {
        //out.println(order[j]);
        // out.println("ORDER FINAL");
    //out.println(order[i]);


out.println("<tr>");
for(int t=0;t<9;t++)
{

out.println("<td>");
out.println(Float.valueOf(str[t]));
out.println(" </td>");


}
out.println("<td>");
//out.println("<a href='http://www.photofuntoos.com'>");

//out.println("<meta http-equiv="refresh",content="0; url=http://example.com/" />");
//response.setContentType("text/html");

      // New location to be redirected
  //    String site = new String("http://www.photofuntoos.com");

    //  response.setStatus(response.SC_MOVED_TEMPORARILY);
     // response.setHeader("Location", site);
String[] tokens = webservices[i].split("/");
//out.println("<a href=tokens[2]>");
//out.println(tokens[2]);
String urladdr="http://"+tokens[2];
//URL x = new URL(urladdr);
//urladdr="http://www.google.com";
//out.println("<a href='http://www.leadtools.net'>");
//out.println("<a href=hello2?urladdr1='http://www.leadtools.net'>");
out.println("<a href=hello2?urladdr1="+urladdr+">");
//out.println("<a href=hello4>");
//out.println(tokens[0]);
out.println(urladdr);
//out.println("http://"+tokens[2]);

//out.println(webservices[i]);
out.println("</a>");
out.println(" </td>");
out.println(" </tr>");
      for(int t=0;t<9;t++)
  {
    //out.println();
    //out.println(str[t]);
           // out.println(Float.valueOf(str[t]));

    //out.println(quality[count][t]);
    }

   // }
    }
            }

    //out.println("Inside countloop");

    //out.println(count);

    //out.println(order[i]);
    count2=count2+1;
            }
/*while(count2<no)
{
    //out.println("Count final");
    //out.println(count2);
    String[] str=i2.next();

    for(i=1;i<2500;i++)
{

    if(count2==order[i])
    {
        // out.println("ORDER FINAL");
    //out.println(order[i]);


out.println("<tr>");
for(int t=0;t<9;t++)
{

out.println("<td>");
out.println(Float.valueOf(str[t]));
out.println(" </td>");


}
out.println("<td>");
//out.println("<a href='http://www.photofuntoos.com'>");

//out.println("<meta http-equiv="refresh",content="0; url=http://example.com/" />");
//response.setContentType("text/html");

      // New location to be redirected
  //    String site = new String("http://www.photofuntoos.com");

    //  response.setStatus(response.SC_MOVED_TEMPORARILY);
     // response.setHeader("Location", site);
String[] tokens = webservices[i].split("/");
//out.println("<a href=tokens[2]>");
//out.println(tokens[2]);
String urladdr="http://"+tokens[2];
//URL x = new URL(urladdr);
//urladdr="http://www.google.com";
//out.println("<a href='http://www.leadtools.net'>");
//out.println("<a href=hello2?urladdr1='http://www.leadtools.net'>");
out.println("<a href=hello2?urladdr1="+urladdr+">");
//out.println("<a href=hello4>");
//out.println(tokens[0]);
out.println(urladdr);
//out.println("http://"+tokens[2]);

//out.println(webservices[i]);
out.println("</a>");
out.println(" </td>");
out.println(" </tr>");
      for(int t=0;t<9;t++)
  {
    //out.println();
    //out.println(str[t]);
           // out.println(Float.valueOf(str[t]));

    //out.println(quality[count][t]);
    }


    }
            }

    //out.println("Inside countloop");

    //out.println(count);

    //out.println(order[i]);
    count2=count2+1;
            }

  */
        } finally {
            out.close();
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
