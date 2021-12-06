
/*AUTOR: TOLEFO Parfait
  email: parfaittolefo23@gmail.com
  Tel  : +229 61474698
        +229 52422809*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   int NbrElect,NbrCand,NbrRes,i,j,PointCandActu=0,l,NomCandGan[50],NomCandCompter[50][50];
   int Point[50],NomCandGang[20][20],PointFort=0,PointGag[50];
   char noms[50][15];
   char Villles[50][15];


   void mettreTabNull(int tab[]){
       int i;
       for(i=0;i<20;i++){
       tab[i]=0;
       }

   }
    // lecrure des entrees du programme

    scanf("%d",&NbrElect);

    for(i=0;i<NbrElect;i++)
    {

        scanf("%d %d",&NbrCand,&NbrRes);



        for(j=0;j<NbrCand;j++)
            {

            scanf("%s",&noms[j]);
            }
            for(j=0;j<NbrRes;j++)
            {

            scanf("%s %d %s",&noms[j],&Point[j],&Villles[j]);

            }


            // Calcul du resultats
             for(l=0;l<NbrRes;l++){

                     for(j=0;j<NbrRes;j++){

                        if(strcmp(noms[l],NomCandCompter[j])!=0 && strcmp(noms[l],noms[j])==0 )
                           {
                               PointCandActu+=Point[j];
                           }

                     }
                     if(PointCandActu>PointFort){

                        PointFort=PointCandActu;
                        PointGag[i]=PointFort;
                        strcpy(NomCandGang[i],noms[l]);
                        strcpy(NomCandCompter[l],noms[l]);
                     }
                     else if (PointCandActu==PointFort){
                             PointGag[i]=0;
                        strcpy(NomCandGang[i]," ");
                        strcpy(NomCandCompter[l],noms[l]);
                     }
                     strcpy(NomCandCompter[j],noms[l]);
                      PointCandActu=0;
                     }
                     PointCandActu=0;
                     PointFort=0;
                     l=0;
                     mettreTabNull(Point);

             }

        for(i=0;i<NbrElect;i++){

         if(PointGag[i]==0)
         {
             printf("\nVOTE %d: THERE IS DILEMMA\n",i+1);
         }

        else
        {
           printf("VOTE %d: HE WINNER IS %s %d\n",i+1,NomCandGang[i],PointGag[i]);
        }
   }

    return 0;
}


