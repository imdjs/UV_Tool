import bpy,os,sys
from mathutils import Vector
from math import *
from ctypes import *

FolderUV=os.path.basename(os.path.dirname(__file__));#IMDJS_green_land
#print("FolderUV==",FolderUV);
if(FolderUV+".global_var" in sys.modules):
    G=sys.modules[FolderUV+".global_var"];
else:
    exec("import "+FolderUV+".global_var as G");#√
        

from .PYLIB_math import*


def  iΔGetCirclecenter_and_radius(f2Head,f2Tail,f2Middle,f3XYR__):
    k1=k2=0;
    x1=(f2Head[0]);y1=(f2Head[1]);x2=(f2Tail[0]);y2=(f2Tail[1]);x3=(f2Middle[0]);y3=(f2Middle[1]);
    print("x1",x1,"y1",y1,"x2",x2,"y2",y2,"x3",x3,"y3",y3,)
    if((y1==y2) and (y2==y3)):
        print("NO\n");
        return  False ;

    elif((y1!=y2)and(y2!=y3)):
        k1=(x2-x1)/(y2-y1);
        k2=(x3-x2)/(y3-y2);
        print("k1=%f  k2=%f\n",k1,k2);

        if((0<=abs(k1-k2)) and (abs(k1-k2)<0.002)) :

            print("NO 2\n");
            #ΔΔ平均拉直()
            return False  ;

    a=(2*(x2-x1));
    b=(2*(y2-y1));
    #print("a=%d\n",a,"b=%d\n",b);
    c=(x2*x2+y2*y2-x1*x1-y1*y1);
    d=(2*(x3-x2));
    e=(2*(y3-y2));
    f=(x3*x3+y3*y3-x2*x2-y2*y2);

    x=(b*f-e*c)/(b*d-e*a);
    y=(d*c-a*f)/(b*d-e*a);

    #print("圆心x为%d\n", x, "圆心y为%d\n",y);
    r=sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1));
    #print("半径为%d\n", r);
    f3XYR__[0]=x;f3XYR__[1]=y;f3XYR__[2]=r;
    # return  f3XYR__;
    return True ;


##---------------------------------------------------------------------------------------
def  fΔthreepoints_radian( f2Head, f2Tail, f2Circlecenter):
    fEdge1=sqrt( pow((f2Head[0]-f2Circlecenter[0]),2)+pow((f2Head[1]-f2Circlecenter[1]),2) ) ;
    fEdge2=sqrt( pow((f2Tail[0]-f2Circlecenter[0]),2)+pow((f2Tail[1]-f2Circlecenter[1]),2) );
    fEdgeOpp=sqrt( pow((f2Head[0]-f2Tail[0]),2)+pow((f2Head[1]-f2Tail[1]),2));
    cosA=( fEdge1*fEdge1+fEdge2*fEdge2-fEdgeOpp*fEdgeOpp)/(2*fEdge1*fEdge2 );#角度只能从0到180度 没有负角度
    fRadianOpp=acos(cosA );##cos值 从-1到1
    return fRadianOpp;

def  fΔRadinpuls( f2Head, f2Circlecenter, fRadinpuls, bClockwise):
    #fXHeadminus,fYHeadminus,fHeadradian十,fRadianpuls十;
    fXHeadminus=f2Head[0]-f2Circlecenter[0]; fYHeadminus=f2Head[1]-f2Circlecenter[1];
    f2XY=[fXHeadminus,fYHeadminus];
    fHeadradian十=atan3(f2XY[0],f2XY[1]);
    #print("fHeadradian十%d\n", fHeadradian十,  "角%d\n",degrees(fHeadradian十))
    if( bClockwise):
        if((fRadinpuls+fHeadradian十)<piΧ2):fRadianpuls十=fRadinpuls+fHeadradian十;
        if((fRadinpuls+fHeadradian十)>piΧ2):fRadianpuls十=(fRadinpuls+fHeadradian十)-piΧ2;
        if((fRadinpuls+fHeadradian十)>piΧ2*2):fRadianpuls十=(fRadinpuls+fHeadradian十)-piΧ2*2;
        else:fRadianpuls十=(fRadinpuls+fHeadradian十)-piΧ2;

    else:
        if((fRadinpuls+fHeadradian十)<piΧ2):fRadianpuls十=-fRadinpuls+fHeadradian十;
        if((fRadinpuls+fHeadradian十)>piΧ2):fRadianpuls十=(-fRadinpuls+fHeadradian十)-piΧ2;
        if((fRadinpuls+fHeadradian十)>piΧ2*2):fRadianpuls十=(-fRadinpuls+fHeadradian十)-piΧ2*2;
        else:fRadianpuls十=(-fRadinpuls+fHeadradian十)-piΧ2;

    if (fRadianpuls十<0):##如果  弧为负
        fRadianpuls十=fRadianpuls十+piΧ2;
    #print("fRadianpuls十%d\n", fRadianpuls十,"角%d\n",degrees(fRadianpuls十) , "fRadinpuls%d\n", fRadinpuls,"角%d\n",degrees(fRadinpuls) )
    return fRadianpuls十;
    
#==============================================================
def Δradian_f2(fRadianpuls十, fRadus,  f2Circlecenter, f2ver__):
    fX=fRadus*cos(fRadianpuls十);fY=fRadus*sin(fRadianpuls十);
    f2VerFake=[fX,fY];
    #print("fX", fX,"fY", fY )
    if (fX and fY):
        #f2VerFake[2]=fX,fY;
        f2十f2_f2(f2VerFake,f2Circlecenter,f2ver__);
        #print("f2入点Fake%d\n", f2VerFake, "f2入点Real%d\n",f2点Real);
    #else
        #print("求不到点f2Real");

#==============================================================
def  bΔisClockwise (f2Head, f2Middle, f2Tail, f2Circlecenter):
    f2Minus=[None,None];
    f2一f2_f2(f2Head,f2Circlecenter,f2Minus);fHead弧十=atan3(f2Minus[0],f2Minus[1]);
    f2一f2_f2(f2Middle,f2Circlecenter,f2Minus);f中弧十=atan3(f2Minus[0],f2Minus[1]);
    f2一f2_f2(f2Tail,f2Circlecenter,f2Minus);fTail弧十=atan3(f2Minus[0],f2Minus[1]);
    if ((fHead弧十<f中弧十 and f中弧十<fTail弧十)or( f中弧十<fTail弧十 and fTail弧十<fHead弧十 )or( fTail弧十<fHead弧十 and fHead弧十 <f中弧十)):
       bClockwise=True ;
    else:
       bClockwise=False ;
    return bClockwise;


#/////////////////////////////////////////
def ΔUVsmooth(LvMeshVerCo,LuvSelected,fLengthFac,LuvResult__):
    iAllNumVer=LuvSelected.__len__();iAllNumVer一1=iAllNumVer-1;
    if(iAllNumVer<2):
        return ;

    Vv乛pre=[0]*iAllNumVer;VfLengthRealPer=[0]*iAllNumVer;VfLengthRealPerAdd=[0]*iAllNumVer;
    fRealLengthPerAdd=0;fMeshLengthAdd=0;fThisUVLengthAdd=0;LfMeshLengthPer=[0]*iAllNumVer;

    for ξ点 in range(1,iAllNumVer):
        ξ点pre=ξ点-1;
        #----原始节长------------------------------------------------------
        v乛pre=LuvSelected[ξ点pre]-LuvSelected[ξ点];
        #printf("ξ点=  %d  =  %f  =  %f  \n",ξ点,v乛pre[0],v乛pre[1]);
        fThisRealLength=v乛pre.length;Vv乛pre[ξ点]=v乛pre;
        VfLengthRealPer[ξ点]=fThisRealLength;#printf("VfLengthRealPer=%f\n",VfLengthRealPer[ξ点]);
        fRealLengthPerAdd+=fThisRealLength;
        VfLengthRealPerAdd[ξ点]=fRealLengthPerAdd;#[0,f,f,f,f]
        #----网--------------------------
        fMeshThisLength=(LvMeshVerCo[ξ点pre]-LvMeshVerCo[ξ点]).length;
        LfMeshLengthPer[ξ点]=fMeshThisLength;
        fMeshLengthAdd+=fMeshThisLength;

    fLengthPer=fRealLengthPerAdd/iAllNumVer一1;
    fAllUVLengthΞAllMeshLength=VfLengthRealPerAdd[iAllNumVer一1]/fMeshLengthAdd;
    #printf("Lflen=",VfLengthRealPer.size());

    #-----------------------------------------------------------------
    #☐☐☐f节长per
    #☐┃━━━━━┃━━━━━┃━━━━━┃━━━→┃☐f平均累此点长艹☐ξ点
    #☐☐☐☐☐☐☐↓☐☐☐☐☐↓☐☐☐☐☐↓☐☐☐☐↓☐☐☐☐☐☐☐☐    
    #☐┃←┃←┃←━━━━━━━━━┃←━━━━━━┃☐v此乛前节☐☐ξ点now☐☐
    #☐☐☐☐☐☐☐┃f此点长一累此点长十┃☐
    #☐┃←━━━━━━━━━━━━┃←━━┃←━┃←┃☐v此乛前节☐☐ξ点now☐☐
    #☐☐☐☐☐☐☐┃f此点长一累此点长十┃☐
    #----比较----------------------------------------------------------
    ξ点now=1;LuvResult__[0]=LuvSelected[0];LuvResult__[-1]=LuvSelected[-1];
    for ξ点 in range(1,iAllNumVer一1):
        ξ点pre=ξ点-1;
        fThisUVLengthNow=LfMeshLengthPer[ξ点] *fAllUVLengthΞAllMeshLength;#●按网的比例
        fThisUVLengthAdd+=( fLengthPer+( fThisUVLengthNow-fLengthPer ) *fLengthFac );#●累加每节正负偏移后的长,总的正负偏移量为零
        while(ξ点now<iAllNumVer):
            fThisUVLength一ThisUVLengthAdd=VfLengthRealPerAdd[ξ点now]-fThisUVLengthAdd;#看是否长了,长了的这节就以这节为方向偏移
            #----只往后偏移  实比精简长或等的点------------------------------------
            if(fThisUVLength一ThisUVLengthAdd>=0):#找到偏移的方向段
                fOffsetProportion=fThisUVLength一ThisUVLengthAdd/VfLengthRealPer[ξ点now];#比例 决定uv精简偏移量   一定在原来方向上偏移
                v乛pre=Vv乛pre[ξ点now];vOffsetBack=v乛pre*fOffsetProportion;
                vVerLoc=vOffsetBack+LuvSelected[ξ点now];
                LuvResult__[ξ点]=vVerLoc;

                #----超过了几节--------------------------
                if(fThisUVLength一ThisUVLengthAdd>fLengthPer):
                    break;#ξ点now 停止

                ξ点now+=1;
                break;

            ξ点now+=1;
    print("LuvResult__==",LuvResult__);
    
#==============================================================
def  ΔStraightenUV(iNumOfSelectedvers, f2UVHead, f2UVTail, LuvResult__):
    f2UVVecOffsetFake=[None,None];f2UVHead乛Tail=[None,None];f2UVMul=[None,None];
    f2一f2_f2(f2UVTail,f2UVHead,f2UVHead乛Tail);#求从零点开始的线总Length向
    fAllLength=LengthF2(f2UVHead,f2UVTail);  fPerUvLength=fAllLength/(iNumOfSelectedvers-1);
    fPerLengthΞAllLength=fPerUvLength/fAllLength;
    for i in range(iNumOfSelectedvers):
        f2Χf_f2(f2UVHead乛Tail,fPerLengthΞAllLength*i,f2UVMul);#从零点开始的当前点线向
        f2十f2_f2(f2UVMul,f2UVHead,LuvResult__[i]);#移动到uvHead的当前点线向


#==============================================================
def  f2Δf2VerticalOffset(iNumOfSelectedvers,iLayer,LuvResult__, LfMeshperVerticallength十Add, f2LastLayerFirstGroupCo):
    f2SideEdge乛=[None,None];f2SlopeEdge乛=[None,None];f2OppEdge乛=[None,None];

    f2一f2_f2(LuvResult__[iNumOfSelectedvers-1],LuvResult__[0],f2SideEdge乛);#即第壹行的总Length向
    f2一f2_f2(f2LastLayerFirstGroupCo,LuvResult__[0],f2SlopeEdge乛);
    fΔGetVectorOfAngle(f2SideEdge乛,f2SlopeEdge乛,f2OppEdge乛);
    f2LocOfVertical=[None,None];f2十f2_f2(LuvResult__[0],f2OppEdge乛,f2LocOfVertical);#把f2对边向 移到实际丅
    f2VecOfVerticalOffset=[None,None];f2一f2_f2(f2LastLayerFirstGroupCo,f2LocOfVertical,f2VecOfVerticalOffset);

    #----求虚拟应偏移向----------------------------------------------------------------------
    if(bpy.context.window_manager.bpXYwm  and G.fAllParallelLengthG):
        fAllVecOffsetLength=LengthF2([0,0],  f2VecOfVerticalOffset);
        fAllVerticalMeshLength=LfMeshperVerticallength十Add[iLayer-2];
        fVerticalΞParallelMesh=fAllVerticalMeshLength/G.fAllParallelLengthG;fAllParallelUVLength=LengthF2([0,0],  f2SideEdge乛);
        fVirtualOffsetΞRealOffset=(fAllParallelUVLength*fVerticalΞParallelMesh)/fAllVecOffsetLength;
        #print("TOTAL UV==",fAllVecOffsetLength,fAllParallelUVLength);
        f2VecOfVerticalOffset=[f2VecOfVerticalOffset[0]*fVirtualOffsetΞRealOffset,f2VecOfVerticalOffset[1]*fVirtualOffsetΞRealOffset];
        #print("TOTAL OFFSET==",f2VecOfVerticalOffset);

    return f2VecOfVerticalOffset;

#==============================================================
def ΔTransParallelpoints(iNumOfSelectedvers,iLayerAll, iLayer,f2VecOfVerticalOffset, LuvResult__, bIsVertical,LfMeshperVerticallength十Add , Lf2UVVerticalParallelLine):
    f2每个组偏移向=[0.0,0.0];
    if(bIsVertical):
        fProportionThis=LfMeshperVerticallength十Add[iLayer-1]/LfMeshperVerticallength十Add[iLayerAll-2];#
        f2每个组偏移向[0]=f2VecOfVerticalOffset[0]*fProportionThis;f2每个组偏移向[1]=f2VecOfVerticalOffset[1]*fProportionThis;
    else:
        f2每个组偏移向[0]=f2VecOfVerticalOffset[0]/(iLayerAll-1)*iLayer;f2每个组偏移向[1]=f2VecOfVerticalOffset[1]/(iLayerAll-1)*iLayer;

    for i组 in range(iNumOfSelectedvers):
        f2十f2_f2(LuvResult__[i组],f2每个组偏移向,Lf2UVVerticalParallelLine[i组]);

#==============================================================
def  ΔAutoAlignUV(iNumOfSelectedvers, f2UVHead, f2UVTail,ipLMR, Lf2UV应Real序__) :
    f2UVVecOffsetFake=[None,None];f2UVHead乛Tail=[None,None];f2UVMul=[None,None];fAllLength=0.00000001;
    f2一f2_f2(f2UVTail,f2UVHead,f2UVHead乛Tail);#求从零点开始的线总Length向
    print("UV=",f2UVTail,f2UVHead,f2UVHead乛Tail);
    if(f2UVHead乛Tail[0]==0):
        f2UVHead乛Tail[0]=0.0001;
    fAtan=(f2UVHead乛Tail[1]/f2UVHead乛Tail[0]);
    #print("f2UV差前%f  %f    ",f2UVHead乛Tail[0],f2UVHead乛Tail[1]);
    #----在←→--------------------------
    if(1>fAtan and fAtan >=-1):
        fAllLength=abs(f2UVHead乛Tail[0]);
        if(ipLMR==2):
            f2UVHead[1]=f2UVTail[1];
        elif(ipLMR==1):
            f2UVHead[1]+=(f2UVHead乛Tail[1]/2);
            
        f2UVHead乛Tail[1]=0;
        #归零UVx 把uvHead移动HeadTail两点轴的中间#print("在←→     ");
    #----在↑↓--------------------------
    else:
        fAllLength=abs(f2UVHead乛Tail[1]);
        if(ipLMR==2):
            f2UVHead[0]=f2UVTail[0];
        elif(ipLMR==1):
            f2UVHead[0]+=(f2UVHead乛Tail[0]/2);
        
        f2UVHead乛Tail[0]=0;#归零UVy#print("在↑↓    ");

    fPerUvLength=fAllLength/(iNumOfSelectedvers-1);
    fPerLengthΞAllLength=fPerUvLength/fAllLength;##print("fPerLengthΞAllLength  与总Length%f  %f\n",fPerLengthΞAllLength,fAllLength);
    #print("f2UV差后%f  %f\n",f2UVHead乛Tail[0],f2UVHead乛Tail[1]);
    #print("f2UVHead后 %f    %f\n",f2UVHead[0],f2UVHead[1]);
    
    for i in range( iNumOfSelectedvers):
        f2Χf_f2(f2UVHead乛Tail,fPerLengthΞAllLength*i,f2UVMul);#从零点开始的当前点线向
        #print("f2UVMul=%f  %f\n",f2UVMul[0],f2UVMul[1]);
        f2十f2_f2(f2UVMul,f2UVHead,Lf2UV应Real序__[i]);#移动到uvHead的当前点线向
        #print("Lf2UV应Real序__[i]=%f   %f\n",Lf2UV应Real序__[i][0],Lf2UV应Real序__[i][1]);

#==============================================================
#print ("DLL是-----------------",_卐DLL.dll)
def f2Δuv_f2(uv):
    return (c_float*2)(uv[0],uv[1]);


def LLf3ΔGetListOfSelectedVerCo (iNumOfSelectedvers):
    #iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG[0]);
    iilayer=G.LlayLLisamelocloop_igroup_ξVerG.__len__()-1;
    LvMeshVerCo=[None]*iNumOfSelectedvers;
    #LvVerticalVerCo=((c_float*3)*(iilayer+int(G.bAllclosedselectedversG)))();
    LvVerticalVerCo=[None for f in  range(iilayer+int(G.bAllclosedselectedversG))];
    id= bpy.context.active_object.data ; #:type: id
    Cmuvl = id.uv_layers.active.data ;
    Lmv=id.vertices;

    for iOrd in range( iNumOfSelectedvers):
        #print("PointIndex==",G.LlayLLisamelocloop_igroup_ξVerG[0][iOrd]);
        mv=Lmv[G.LlayLLisamelocloop_igroup_ξVerG[0][iOrd][2]];
        LvMeshVerCo[iOrd]=mv.co;
    for iLay in range(iilayer):#找到每层第壹个点丅
        #print("PointIndex==",G.LlayLLisamelocloop_igroup_ξVerG[iLay][0][2]);
        mv=Lmv[G.LlayLLisamelocloop_igroup_ξVerG[iLay][0][2]];
        LvVerticalVerCo[iLay]=mv.co;
        #print("CoX==",mv.co.x,LvVerticalVerCo[iLay][0]);
    
    #----圆心--------------------------
    if(G.bAllclosedselectedversG):
        #print("ALL CLOSE",);
        if(G.ξCirclePointG!=None):
            mv=Lmv[G.ξCirclePointG];
            LvVerticalVerCo[LvVerticalVerCo.__len__()-1]=mv.co;
        else:
            vAdd=Vector((0,0,0));
            for ξ点序,LLiSamelocloop_igroup_ξVer in enumerate( G.LlayLLisamelocloop_igroup_ξVerG[iilayer-1]):#计算最后一层的点丅平均值。
                mv=Lmv[LLiSamelocloop_igroup_ξVer[2]];
                vAdd+=mv.co;
            vEverage=vAdd/(iNumOfSelectedvers);
            LvVerticalVerCo[LvVerticalVerCo.__len__()-1]=Vector(( vEverage[0],  vEverage[1], vEverage[2] ));
        #print("LAYER==",iilayer,len(LvVerticalVerCo));
        LvVerticalVerCo.reverse();
    return  (LvMeshVerCo,LvVerticalVerCo);

#==============================================================
def bΔGetLinkedSelectedLine(id,Cmuvl,LiAllTriFaceGroup,DigroupLiSelectedLR_,Diloop_igroupAll,Dsallloopξver_,DiallgroupLLξface_Liloop_):
    #---把相同丅环加入组----------------------------------------------------------
    LiNumgroup=0;#Li已入组的环=[];#LLi环f2UVAll=[];#LLi环f2UV比较All=[];
    #---查找Di全部环i组 ----------------------------------------
    #先找出四个共面的组，然后再把少于四个共面的组根据uv分组
    DξVerLiloopAll={};Cmv=id.vertices;
    #---检测第壹组有无三角面------------------------------------------------------------
    if(Diloop_igroupAll=={}):
        if(not bpy.context.window_manager.bpTransmition):
            for ξFace,mpAll in enumerate(id.polygons):
                if(mpAll.select==False):continue;
                b线选=False;iFacePoint=len(mpAll.loop_indices);
                if(G.bIsTriangleG):
                    break;
                if(not G.bIsTriangleG and iFacePoint==3):
                    for i步3 in range(iFacePoint): #如果是四边面 len等于4 如果是三角面len等于3，
                        i步3下步 = (i步3+1) % iFacePoint;
                        ξVer = mpAll.vertices[i步3];#Vertex indices 如果是四边面 len等于4 如果是三角面len等于3
                        ξVerNext = mpAll.vertices[i步3下步];
                        iLoop=mpAll.loop_indices[i步3];
                        ξLoopNext=mpAll.loop_indices[i步3下步];

                        bSelectedmuvll1 = False;bSelectedmuvll2=False ;

                        if(not Cmv[ξVer].hide and  Cmv[ξVer].select):#只有显示网格的uv选线才算数
                            bSelectedmuvll1= Cmuvl[iLoop].select; #mpAll.loop_indices[i步3] 为MeshUVLoop的ξ
                        if(not Cmv[ξVerNext].hide and  Cmv[ξVer].select):#只有显示的uv选线才算数
                            bSelectedmuvll2= Cmuvl[ξLoopNext].select;

                        if (bSelectedmuvll1 and bSelectedmuvll2):# 如果一条线两点被选中
                            G.bIsTriangleG=True;#print("TRIANGLE",);
                            break;

        #----------------------------------------------------------------------------
        for ξFace,mpAll in enumerate(id.polygons):
            if(mpAll.select==False):continue;
            b线选=False;iFacePoint=len(mpAll.loop_indices);
            for i步3 in range(iFacePoint): #如果是四边面 len等于4 如果是三角面len等于3，
                i步3下步 = (i步3+1) % iFacePoint;
                ξVer = mpAll.vertices[i步3];#Vertex indices 如果是四边面 len等于4 如果是三角面len等于3
                ξVerNext = mpAll.vertices[i步3下步];
                iLoop=mpAll.loop_indices[i步3];
                ξLoopNext=mpAll.loop_indices[i步3下步];

                bSelectedmuvll1 = False;bSelectedmuvll2=False ;
                """
                if(bpy.context.scene.tool_settings.use_uv_select_sync== True):
                    bSelectedmuvll1= id.vertices[ξVer].select;
                    bSelectedmuvll2= id.vertices[ξVerNext].select;
                else:
                """
                if(not Cmv[ξVer].hide and Cmv[ξVer].select):#只有显示的uv选线才算数
                    bSelectedmuvll1= Cmuvl[iLoop].select; #mpAll.loop_indices[i步3] 为MeshUVLoop的ξ
                if(not Cmv[ξVerNext].hide and Cmv[ξVer].select):#只有显示的uv选线才算数
                    bSelectedmuvll2= Cmuvl[ξLoopNext].select;

                if(bpy.context.window_manager.bpTransmition or G.bIsTriangleG==True):
                    if(ξVer not in DξVerLiloopAll):
                        DξVerLiloopAll[ξVer]=[];
                    if(iLoop not in DξVerLiloopAll[ξVer]):
                        DξVerLiloopAll[ξVer].append(iLoop);#{i组:[iLoop,iLoop]}
                elif(not bpy.context.window_manager.bpTransmition ):
                    if (bSelectedmuvll1):# 如果有一点被选中
                        if(ξVer not in DξVerLiloopAll):
                            DξVerLiloopAll[ξVer]=[];
                        if(iLoop not in DξVerLiloopAll[ξVer]):
                            DξVerLiloopAll[ξVer].append(iLoop);#{i组:[iLoop,iLoop]}

                #----------------------------------------------------------------------------
                if(str(iLoop) not in Dsallloopξver_):
                    Dsallloopξver_[str(iLoop)]=ξVer;

        #print("D All IP,R",DξVerLiloopAll);

        #---根据uv丅分组-----------------------------------------------------------------

        for  ξVer,Liloop in  DξVerLiloopAll.items():
            LLiSameUVloop=[];iSameVerDiffuvgroupnum=0;LiHaveComLoop=[];
            for i比较步,iComLoop in  enumerate(Liloop):#迭代一个点内的多个环
                if(iComLoop in LiHaveComLoop):#如果已经找到与比较环相等的环，就不用再新建比较环
                    continue;
                uvComLoop=Cmuvl[iComLoop].uv;LLiSameUVloop.append([]);#新几个表示共有几组环 不相等
                LLiSameUVloop[iSameVerDiffuvgroupnum].append(iComLoop);
                LiHaveComLoop.append(iComLoop);
                for i步,iLoop in  enumerate(Liloop):#迭代一个点内的多个环
                    if(i比较步!=i步 and uvComLoop==Cmuvl[iLoop].uv and iLoop not in LiHaveComLoop):#找到一个与比较环相等的环
                        LLiSameUVloop[iSameVerDiffuvgroupnum].append(iLoop);#[[iLoop,iLoop],[iLoop,iLoop]]
                        LiHaveComLoop.append(iLoop);
                iSameVerDiffuvgroupnum+=1;

            if(len(LLiSameUVloop)<2 ):#如果此点带四个环
                for i步,iLoop in  enumerate(Liloop):
                    Diloop_igroupAll[iLoop]=LiNumgroup;
                LiNumgroup+=1;#增加一个组

            else:#有多个不同uv的环
                for i组,LiSameUVloop in  enumerate(LLiSameUVloop):
                    for iSameUVloop in  LiSameUVloop:
                        Diloop_igroupAll[iSameUVloop]=LiNumgroup;
                    LiNumgroup+=1;#增加一个组
        #---记录到网格属性-----------------------------------------------------------------
        """
        id["UV_TOOL"]["fUV"]=Cmuvl[0].uv[0];
        id["UV_TOOL"]["iPOLY"]=len(id.polygons);
        id["UV_TOOL"]["ALL_R_G"]=Diloop_igroupAll;
        id["UV_TOOL"]["ALL_R_IP"]=Dsallloopξver_;
        """
    #print("D All  R:G==",Diloop_igroupAll);
    #return ;
    #---填充  DigroupLiSelectedLR_,DiallgroupLLξface_Liloop_---------------------------
    LLξface_Liloop_=[];
    for ξFace,mpAll in enumerate(id.polygons):
        if(mpAll.select==False):continue;
        b线选=False;iFacePoint=len(mpAll.loop_indices);
        for i步3 in range(iFacePoint): #如果是四边面 len等于4 如果是三角面len等于3，
            #i步=None;i步=None;i步=None;i步=None;
            i步3下步 = (i步3+1) %iFacePoint;#3%4=3  ; 4%3=1;4%4=0
            ξVer = mpAll.vertices[i步3];#Vertex indices 如果是四边面 len等于4 如果是三角面len等于3
            ξVerNext = mpAll.vertices[i步3下步];
            iLoop=mpAll.loop_indices[i步3];
            ξLoopNext=mpAll.loop_indices[i步3下步];
            bSelectedmuvll1 = False;bSelectedmuvll2=False ;
            """
            if(bpy.context.scene.tool_settings.use_uv_select_sync== True):
                bSelectedmuvll1= id.vertices[ξVer].select;
                bSelectedmuvll2= id.vertices[ξVerNext].select;
            else:
            """
            if(not Cmv[ξVer].hide and Cmv[ξVer].select):#只有显示的uv选线才算数
                bSelectedmuvll1= Cmuvl[iLoop].select; #mpAll.loop_indices[i步3] 为MeshUVLoop的ξ
            if(not Cmv[ξVerNext].hide and Cmv[ξVer].select):#只有显示的uv选线才算数
                bSelectedmuvll2= Cmuvl[ξLoopNext].select;
            #--------------------------------------------------------------------------
            if(bpy.context.window_manager.bpTransmition or G.bIsTriangleG==True):
                i组转=Diloop_igroupAll[iLoop];
                i组下转=Diloop_igroupAll[ξLoopNext];

                if(i组转 not in DiallgroupLLξface_Liloop_):
                    LLξface_Liloop_=DiallgroupLLξface_Liloop_[i组转]=[[],[]];#{i组转:[[ξFace,ξFace],[iLoop,iLoop]],}
                    LLξface_Liloop_[0]=[0]*4;LLξface_Liloop_[1]=[0]*4;LLξface_Liloop_[0]. clear();LLξface_Liloop_[1]. clear();#reserve;
                LLξface_Liloop_=DiallgroupLLξface_Liloop_[i组转];
                
                if(ξFace not in DiallgroupLLξface_Liloop_[i组转][0]):
                    LLξface_Liloop_[0].append(ξFace);

                if(mpAll.loop_indices[i步3] not in DiallgroupLLξface_Liloop_[i组转][1]):
                    LLξface_Liloop_[1].append(mpAll.loop_indices[i步3]);

            else:
                if (bSelectedmuvll1):# 如果一点被选中
                    i组转=Diloop_igroupAll[iLoop];

                    if(i组转 not in DiallgroupLLξface_Liloop_):
                        LLξface_Liloop_=DiallgroupLLξface_Liloop_[i组转]=[[],[]];#{i组转:[[ξFace,ξFace],[iLoop,iLoop]],}
                        LLξface_Liloop_[0]=[0]*6;LLξface_Liloop_[1]=[0]*6;LLξface_Liloop_[0]. clear();LLξface_Liloop_[1]. clear();#reserve;
                    LLξface_Liloop_=DiallgroupLLξface_Liloop_[i组转];
                    
                    if(ξFace not in DiallgroupLLξface_Liloop_[i组转][0]):
                        LLξface_Liloop_[0].append(ξFace);
        
                    if(iLoop not in DiallgroupLLξface_Liloop_[i组转][1]):
                        LLξface_Liloop_[1].append(iLoop);

            if (bSelectedmuvll1 and bSelectedmuvll2):# 如果一条线两点被选中
                i组下转=Diloop_igroupAll[ξLoopNext];
                b线选=True;
                if(i组转 not in DigroupLiSelectedLR_):#{i组此:[i组左,i组右],}
                   DigroupLiSelectedLR_[i组转]=[0]*4;DigroupLiSelectedLR_[i组转].clear();#reserve;
                if(i组下转 not in DigroupLiSelectedLR_):
                   DigroupLiSelectedLR_[i组下转]=[0]*4;DigroupLiSelectedLR_[i组下转].clear();#reserve;
                   
                if(i组转 not in DigroupLiSelectedLR_[i组下转]):
                   DigroupLiSelectedLR_[i组下转].append(i组转);
                if(i组下转 not in DigroupLiSelectedLR_[i组转]):
                   DigroupLiSelectedLR_[i组转].append(i组下转);

                    #{ i组转:[ [iLoop,iLoop],[ξFace,ξFace] ],i组转:[[iLoop,iLoop],] }

    #---找出第壹层的前两个组-------------------------------------------------------------------
    #print("D  LR==",DigroupLiSelectedLR_);
    if(len(DigroupLiSelectedLR_)<2):#确定是否选了两点以上
        return False;
    #print("D all G,LLiFiR==",DiallgroupLLξface_Liloop_);
    i组随机=None;b闭合=True;G.LlayLLisamelocloop_igroup_ξVerG.append([]);#第壹层
    for i组此, LiGroupLR in DigroupLiSelectedLR_.items():#返回 键与值的列表
        i组随机=i组此;
        if (len(LiGroupLR)==1):#此点没有左右两点  {i组此:[i组左]}
            Liloop=DiallgroupLLξface_Liloop_[i组此][1];
            #print("Li1=",Liloop);
            G.LlayLLisamelocloop_igroup_ξVerG[0].append([  Liloop,i组此,Dsallloopξver_[str(Liloop[0])]]); #其中一个终组  [[i组此,ξFace]]
            Liloop2=DiallgroupLLξface_Liloop_[LiGroupLR[0]][1];
            G.LlayLLisamelocloop_igroup_ξVerG[0].append([  Liloop2  ,LiGroupLR[0], Dsallloopξver_[str(Liloop2[0])]]);# [[i组此,ξFace],[i组左,ξFace]]  添加第貮个组
            b闭合=False;
            break;

    if(b闭合==True):
        Liloop=DiallgroupLLξface_Liloop_[i组随机][1];LiGroupLR=DigroupLiSelectedLR_[i组随机];
        Liloop2=DiallgroupLLξface_Liloop_[LiGroupLR[0]][1];
        G.LlayLLisamelocloop_igroup_ξVerG[0].append([  Liloop,i组随机,Dsallloopξver_[str(Liloop[0]) ]]) #Head一个点
        G.LlayLLisamelocloop_igroup_ξVerG[0].append([  Liloop2  ,LiGroupLR[0], Dsallloopξver_[str(Liloop2[0])]])#第貮个点


    #--------------------------------------------------------------------------
    #print("bΔGetLinkedSelectedLine==",DiallgroupLLξface_Liloop_);
    #print("0LayADD 2 RingGroup",len(G.LlayLLisamelocloop_igroup_ξVerG[0]),G.LlayLLisamelocloop_igroup_ξVerG[0]);
    return True;
    #print("DigroupLR==",DigroupLiSelectedLR_);
    

    #return (G.iLayerG,L层Di全部选点ξLi环);
#==============================================================
def LLLiΔArangeSelectedVers(self):
    if(bpy.context.scene.tool_settings.uv_select_mode not in ["VERTEX","EDGE"]):
        self.report({"ERROR"},"only works in vertex or edge mode");#"INFO" "ERROR" "DEBUG" "WARNING"
        bpy.context.scene.tool_settings.uv_select_mode="VERTEX";

    bpy.ops.object.mode_set(mode='OBJECT');
    id = bpy.context.active_object.data ;
    if (not  id.uv_layers.active):
        return (None,None,None);
    Cmuvl = id.uv_layers.active.data ;#UVLoopLayers.MeshUVLoopLayer.LMeshUVLoop
    LiAllTriFaceGroup=[];
    DiallgroupLLξface_Liloop={};DithisgroupLξgroupLRsel={};
    G.LlayLLisamelocloop_igroup_ξVerG=[];#[[[iLoop,iLoop],i组转],[[iLoop,i环i,环,iLoop],i组转]]
    LξFaceHaveBeenChecked=[];Liloopcirclecenter=[];
    b闭=None;b全闭=None ;
    G.bAllclosedselectedversG=False;
    G.iLayerG=0;
    G.iCirclecenterGroupG=None;
    G.ξCirclePointG=None;
    G.bIsTriangleG=False;

    Diloop_igroupAll={};
    Dsallgroupξver={};

    bIsFinded=bΔGetLinkedSelectedLine(id,Cmuvl,LiAllTriFaceGroup,DithisgroupLξgroupLRsel,Diloop_igroupAll,Dsallgroupξver,DiallgroupLLξface_Liloop);
    if(not bIsFinded):
        self.report({"ERROR"},"NO LINE LINK");#"INFO" "ERROR" "DEBUG" "WARNING"
        return (None,None,None);
    #ΔΔ判断是否封闭(G.iLayerG,G.LlayLLisamelocloop_igroup_ξVerG,DithisgroupLξgroupLRsel,L层Di全部选点ξLi环);
    #return (Cmuvl,Liloopcirclecenter);
    #---排列第壹层的组-G.LlayLLisamelocloop_igroup_ξVerG[0]-----------------------------------------------
    if (len(G.LlayLLisamelocloop_igroup_ξVerG[0])>1):#如果  选了两个组以上
        i计数 = len(DithisgroupLξgroupLRsel);
        #print ("iCount",i计数)
        b连续 = True ;i第壹个组=None;
        while (b连续==True  and 0 < i计数):
            LiGroupLR = DithisgroupLξgroupLRsel[G.LlayLLisamelocloop_igroup_ξVerG[0][-1][1]];#刚开始Li组左右是第貮个点的组左右，即第壹点与第三点
            #print ("LiGroupLR",LiGroupLR)
            #print("G.LlayLLisamelocloop_igroup_ξVerG[-1]", G.LlayLLisamelocloop_igroup_ξVerG[-1])
            for i, i组左右 in enumerate( LiGroupLR): #刚开始  i组左右是第壹个点 或 第三点
                if ( i组左右 == G.LlayLLisamelocloop_igroup_ξVerG[0][-2][1]):#如果  i组左右  是  此点的前一个点# 刚开始是第壹个点
                    if(i计数 == len(DithisgroupLξgroupLRsel)):
                        i第壹个组=i组左右;
                        #print("FirstG==",i第壹个组);
                    #print ("i组左右 == G.LlayLLisamelocloop_igroup_ξVerG[-2]",i组左右, G.LlayLLisamelocloop_igroup_ξVerG[-2])

                    if(len(LiGroupLR)>1 and LiGroupLR[i-1]==i第壹个组 and i计数<len(DithisgroupLξgroupLRsel)):#密封圆  最后一组为第壹组
                        #print("LastGroup",);
                        i组左右 = LiGroupLR[i-1];
                        b连续= False;
                        break;

                    elif (len(LiGroupLR)>1): #如果  这点连带两个点或以上# 连续选边
                        #print ("1 < len(LiGroupLR)")
                        #else:
                            i组左右= LiGroupLR[i-1];#把此点后一个点  作为 i组左右#刚开始是第三个点
                            #print ("LiGroupLR",LiGroupLR)
                            #print ("G.LlayLLisamelocloop_igroup_ξVerG=",G.LlayLLisamelocloop_igroup_ξVerG)
                    else:#此点 连带 一个点
                        i组左右 = None;
                        b连续= False;
                        #print ("i组左右 = None")
                    break;
            i计数 -= 1;
            #-------------------------------------------------------------------------
            if (i组左右 !=None ):#如果点ξ为0 可能被认为False
                LiLoop=DiallgroupLLξface_Liloop[i组左右][1];
                G.LlayLLisamelocloop_igroup_ξVerG[0].append([ LiLoop ,i组左右,Dsallgroupξver[str(LiLoop[0])]]);
                #print ("LiGroupLR=",LiGroupLR,"Lξ点从Head到Tail选前=",G.LlayLLisamelocloop_igroup_ξVerG,"i组Head=",i组Head)
                #print ("ξ点比较append",i组左右)
                #b连续= True;

    #print("01LayRingGroupIndex",len(G.LlayLLisamelocloop_igroup_ξVerG[0]),G.LlayLLisamelocloop_igroup_ξVerG[0]);
    if(bpy.context.window_manager.bpTransmition):
        ΔGetParallelLine(id,Cmuvl,LξFaceHaveBeenChecked,Diloop_igroupAll,Dsallgroupξver,DiallgroupLLξface_Liloop);

    #print("==",G.LlayLLisamelocloop_igroup_ξVerG[0][0][1],G.LlayLLisamelocloop_igroup_ξVerG[0][-1][1]);
    if (G.LlayLLisamelocloop_igroup_ξVerG[0][0][1]==G.LlayLLisamelocloop_igroup_ξVerG[0][-1][1]): #全封闭
        G.bAllclosedselectedversG=True;#print("ALL CLOSE 2",);
    if(G.iCirclecenterGroupG):
        Liloopcirclecenter=DiallgroupLLξface_Liloop[G.iCirclecenterGroupG][1];
        G.ξCirclePointG=Dsallgroupξver[str(Liloopcirclecenter[0])];
    #print("LiHartRing==",Liloopcirclecenter,"iHart",G.iCirclecenterGroupG,G.iLayerG);
    print("LLLiΔArangeSelectedVers",len(G.LlayLLisamelocloop_igroup_ξVerG[0]),G.LlayLLisamelocloop_igroup_ξVerG);
    return (Cmuvl,Liloopcirclecenter);

#==============================================================
def CmuvllΔΔGetCmuvll():# 这个只能在物体模式下才能记录数据
    bpy.ops.object.mode_set(mode='OBJECT');
    id = bpy.context.active_object.data ;
    if (not  id.uv_layers.active):
        return {'FINISHED'};
    id=bpy.context.active_object.data;
    return id.uv_layers.active.data ;

#==============================================================
def ΔGetParallelLine(id,Cmuvl,LξFaceHaveBeenChecked,Diloop_igroupAll,Dsallgroupξver,DiallgroupLLξface_Liloop):
    bIsParallel=True;bIsShareFace=False;b最后一层=False;b最后一点=False;bNoCirclecenter=False;LiTriFaceGroup=[];
    #----根据这层组找出下一层组-----------------------------------------------------------------
    #print("LAYER------------",G.iLayerG,G.LlayLLisamelocloop_igroup_ξVerG);
    if(len(G.LlayLLisamelocloop_igroup_ξVerG[0])<1):#如果选点少于两点
        return ;
    for iOrd,LiSamelocloop_igroup_ξVer in  enumerate(G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG]):#迭代下一层的各个组
        #---找到共面ξ------------------------------------------------------------
        i组=LiSamelocloop_igroup_ξVer[1];
        if(iOrd==len(G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG])-1):#如果是最后一组
            i组下=G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG][iOrd-1][1];#把倒数第貮组为组下
            #print("LastShareFace ,Layer ,Len,Gpre",LξShareFace,G.iLayerG,len(G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG]),i组下);
            if(b最后一层==True):
                b最后一点=True;
                #print("Is LastLay&Order",iOrd);

        elif(not b最后一层):
            i组下=G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG][iOrd+1][1];

            LξShareFace=[ξFace for ξFace in DiallgroupLLξface_Liloop[ i组 ][0] if ( ξFace in DiallgroupLLξface_Liloop[i组下][0] and  ξFace not in LξFaceHaveBeenChecked)];#前后两组的共面ξ
            if(G.iLayerG!=0 and( len(DiallgroupLLξface_Liloop[i组][0])<3 and len(DiallgroupLLξface_Liloop[i组下][0])<3)):#最后一层最大共面ξ少于3
                b最后一层=True;

                #print("IS LastLayerZZZZZZZ",);
            """"""
            #print("G,Face ",i组,DiallgroupLLξface_Liloop[ i组 ][0] )
            #print("G,FaceNext ",i组下,DiallgroupLLξface_Liloop[i组下][0])

            #print("FaceRecorded ",LξFaceHaveBeenChecked);
            #print("ShareFace---",LξShareFace);

            #print("GROUP",G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG][iOrd][1]);
        if(b最后一层==True and not b最后一点):#最后一层

            i组下=G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG][iOrd+1][1];
            LξShareFace=[ξFace for ξFace in DiallgroupLLξface_Liloop[ i组 ][0] if ( ξFace in DiallgroupLLξface_Liloop[i组下][0] )];
            if(not LξShareFace or  len(LξShareFace)>1):
                """
                if(not LξShareFace ):
                    #print("NOT_SHARE_FACE2",);
                else:
                    #print("SHARE_FACE >1",);
                """
                bIsShareFace=True ;bIsParallel=False ;
            """"""
            #print("G,FaceE ",i组,DiallgroupLLξface_Liloop[ i组 ][0] )
            #print("G,FaceNextE ",i组下,DiallgroupLLξface_Liloop[i组下][0])
            #print("ShareFaceE---",LξShareFace);

        if(not LξShareFace or  len(LξShareFace)>1):
            """"""
            if(not LξShareFace ):
                pass;
                #print("NOT_SHARE_FACE",);
            else:
                pass;
                #print("SHARE_FACE >1",);
            #print("NO BALLANCE",);

            bIsShareFace=True ;bIsParallel=False ;break;
        #----------------------------------------------------------------------------
        try:
            G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG+1];
        except:
            G.LlayLLisamelocloop_igroup_ξVerG.append([]);#增加一层
        if(LξShareFace[0] not in LξFaceHaveBeenChecked):
            LξFaceHaveBeenChecked.append(LξShareFace[0]);

        mpShareFaceTwoGroups=id.polygons[LξShareFace[0]];
        B=False;
        if(len(mpShareFaceTwoGroups.loop_indices)!=4 and len(mpShareFaceTwoGroups.loop_indices)==3):
            for i步3,iLoop in enumerate(mpShareFaceTwoGroups.loop_indices):
                LiTriFaceGroup.append(int(Diloop_igroupAll[iLoop]));
            #print("NOT QUAT",);#当遇到三角面时 最后一层为空[]
            bIsParallel=False;break;

        for i步3 in range(len(mpShareFaceTwoGroups.loop_indices)):#找到并排列下一层组
            i步3下步 = (i步3+1) % len(mpShareFaceTwoGroups.loop_indices);#3%4=3  ; 4%3=1;4%4=0
            ξVer = mpShareFaceTwoGroups.vertices[i步3];#Vertex indices 如果是四边面 len等于4 如果是三角面len等于3
            ξVerNext = mpShareFaceTwoGroups.vertices[i步3下步]
            i组转=int(Diloop_igroupAll[mpShareFaceTwoGroups.loop_indices[i步3]]);
            i组下转=int(Diloop_igroupAll[mpShareFaceTwoGroups.loop_indices[i步3下步]]);
            """"""
            #-----如果是最后第壹组------------------------------------------------------------
            if(iOrd==len(G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG])-1):
                #print("While Last   Group,GroupNext==",i组,i组下);
                if(i组==i组转 and i组下!=i组下转):#顺→
                    #print("exeLast",);
                    G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG+1].append([DiallgroupLLξface_Liloop[i组下转][1],i组下转,ξVerNext]);B=True;break;#
                elif(i组==i组下转 and i组下!=i组转):#逆←
                    #print("exeLast",);
                    G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG+1].append([DiallgroupLLξface_Liloop[i组转][1],i组转,ξVer]);B=True; break;#

            #----十常的组-------------------------------------------------------------
            if(i组==i组转 and i组下!=i组下转):#顺→
                G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG+1].append([DiallgroupLLξface_Liloop[i组下转][1],i组下转,ξVerNext]);B=True;break;
            elif(i组==i组下转 and i组下!=i组转):#逆←
                G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG+1].append([DiallgroupLLξface_Liloop[i组转][1],i组转,ξVer]);B=True;break;

        #if(not B):
            #print("NO NO NO NO,Order==,",iOrd);
    #------找圆心-------------------------------------------------------------
    if(bNoCirclecenter==False):
        i组1=G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG][0][1];i组2=G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG][1][1];#这是未ii层数+1时添加的组
        Li圆心=[i for i in LiTriFaceGroup if(i!=i组1 and i!=i组2)];
        if(Li圆心):
            G.iCirclecenterGroupG=Li圆心[0];
        bNoCirclecenter=True;
        #print("HartGroup==",G.iCirclecenterGroupG);
        #print("Group1==",i组1,"Group2==",i组2);
    #print("Glen,Llen,Layer",len(G.LlayLLisamelocloop_igroup_ξVerG[G.iLayerG]),G.LlayLLisamelocloop_igroup_ξVerG,G.iLayerG);
    if(bIsParallel==True and bIsShareFace==False and b最后一层==False and b最后一点==False):
        G.iLayerG+=1;
        ΔGetParallelLine(id,Cmuvl,LξFaceHaveBeenChecked,Diloop_igroupAll,Dsallgroupξver,DiallgroupLLξface_Liloop);
    #print("ΔGetParallelLine==",G.LlayLLisamelocloop_igroup_ξVerG);  
    
#==============================================================
def Lb_LfΔΔGetLenghtOfVerticalMesh(LvVerticalVerCo):
    bIsVertical=bpy.context.window_manager.bpVerticalDistance ;
    iSize=LvVerticalVerCo.__len__();
    LfMeshperVerticallength十Add=[];LfMeshThisSegmentDistance十=[0]*iSize;
    if(bIsVertical):
        fMeshDistance十Add=0;
        for iOrd,vVerticalMeshCo in enumerate(LvVerticalVerCo):
            if(iOrd==0):continue;
            i此序=iOrd;ipre=iOrd-1;
            vMinus=LvVerticalVerCo[i此序]-LvVerticalVerCo[ipre];
            LfMeshThisSegmentDistance十[iOrd]=fMeshThisSegmentDistance十=vMinus.length;
            fMeshDistance十Add+=fMeshThisSegmentDistance十;
            #LfMeshperVerticallength十Add.append(fMeshDistance十Add);#第壹点不算

        if((len(LvVerticalVerCo)-1)==0):
            fPerMeshLength=fMeshDistance十Add;
        else:
            fPerMeshLength=fMeshDistance十Add/(len(LvVerticalVerCo)-1);

        fMeshDistance十Add=0;
        for iOrd,vVerticalMeshCo in enumerate(LvVerticalVerCo):
            if(iOrd==0):continue;
            i此序=iOrd;ipre=iOrd-1;
            fMeshDistance十Add+=(fPerMeshLength+(LfMeshThisSegmentDistance十[iOrd]-fPerMeshLength)*bpy.context.scene.fpMeshInfulance);
            LfMeshperVerticallength十Add.append(fMeshDistance十Add);#第壹点不算
    #--------------------------------------------------------------------------
    return (bIsVertical,LfMeshperVerticallength十Add);

#==============================================================
def ΔAssignUV(Cmuvl,iNumOfSelectedvers,iilayer,LvVerticalVerCo,LuvResult__,Lf2UVVerticalParallelLine):
    #global G.bAllclosedselectedversG;global G.fAllParallelLengthG;
    if (G.LlayLLisamelocloop_igroup_ξVerG[0][0][1]==G.LlayLLisamelocloop_igroup_ξVerG[0][-1][1]): #全封闭
        G.bAllclosedselectedversG=True;##print("ALL CLOSE",);

    if(G.bAllclosedselectedversG ):#这种情况不能运行否则会出错
        return ;
    #iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG);iilayer=len(G.LlayLLisamelocloop_igroup_ξVerG);
    #-----赋值给第壹层uv---------------------------------------------------------------
    for iOrd, LLiSamelocloop_igroup_ξVer in enumerate(G.LlayLLisamelocloop_igroup_ξVerG[0]):#先排列第壹层
        uvThisVerReal=LuvResult__[iOrd];#此点ξ的uv
        for i环步 in range(  len(LLiSamelocloop_igroup_ξVer[0]) ):#迭代  此点所有  环
            #print("UV is==",uvThisVerReal);
            Cmuvl[ LLiSamelocloop_igroup_ξVer[0][i环步] ].uv=uvThisVerReal;
    #print("//-------------------------------------------------------------------------",);
    #-----赋值给平行层uv------------------------------------------------------------
    #for iLay,LLiSamelocloop_igroup_ξVer in enumerate(G.LlayLLisamelocloop_igroup_ξVerG):
        #print("Lay, LiR,G,IP==",iLay,LLiSamelocloop_igroup_ξVer);

    iLayerReal=iilayer-1;
    #print("LayerCount==",iilayer,iLayerReal);
    if((not bpy.context.window_manager.bpTransmition or iLayerReal<1) or G.bIsTriangleG==True):
        f2LastLayerFirstGroupCo=(c_float*2)(0,0);
    elif(G.LlayLLisamelocloop_igroup_ξVerG[-1]==[]):#最后一层为空 遇到三角形 多建一层
        f2LastLayerFirstGroupCo=f2Δuv_f2(Cmuvl[ G.LlayLLisamelocloop_igroup_ξVerG[-2][0][0][0] ].uv);#最后一层第壹个组丅
        #print("Last Group==", G.LlayLLisamelocloop_igroup_ξVerG[-2][0][1] );
    else:#最后一层为倒数第貮层
        f2LastLayerFirstGroupCo=f2Δuv_f2(Cmuvl[ G.LlayLLisamelocloop_igroup_ξVerG[-2][0][0][0] ].uv);#最后一层第壹个组丅
        #print("Last Group==", G.LlayLLisamelocloop_igroup_ξVerG[-2][0][1] );

    #print("LayLen==",iLayerReal);
    #----计算垂直--------------------------------------------------------------------
    bIsVertical,LfMeshperVerticallength十Add=Lb_LfΔΔGetLenghtOfVerticalMesh(LvVerticalVerCo);

    #----------------------------------------------------------------------------
    f2VecOfVerticalOffset=f2Δf2VerticalOffset(iNumOfSelectedvers,iLayerReal,LuvResult__, LfMeshperVerticallength十Add, f2LastLayerFirstGroupCo);

    for iLayer,LLiSamelocloop_igroup_ξVer in enumerate(G.LlayLLisamelocloop_igroup_ξVerG):
        #print("Lay, LiR,G,IP==",iLayer,LLiSamelocloop_igroup_ξVer);
        #if((not bpy.context.window_manager.bpTransmition or iilayer<4) and iLayer==0):#如果只有两层
            #break;
        if(iLayer==0 or iLayer==iLayerReal):#从第貮层算起作第壹层 倒数一层不用算，因为走最后一层时记录了倒数第貮层，走倒数第貮层时记录了最后一层
            continue;

        ΔTransParallelpoints(iNumOfSelectedvers,iLayerReal, iLayer,f2VecOfVerticalOffset, LuvResult__, bIsVertical,LfMeshperVerticallength十Add , Lf2UVVerticalParallelLine);
        #print("APPLY LAYER",iLayer);
        for iOrd, LiSamelocloop_igroup_ξVer in enumerate(LLiSamelocloop_igroup_ξVer):#先排列第壹层
            uvThisVerReal=Vector((Lf2UVVerticalParallelLine[iOrd][0],Lf2UVVerticalParallelLine[iOrd][1]));#此点ξ的uv

            for i环步 in range(  len(LiSamelocloop_igroup_ξVer[0]) ):#迭代  此点所有  环
                Cmuvl[ LiSamelocloop_igroup_ξVer[0][i环步] ].uv=uvThisVerReal;


#////////////////////////////////////////////////
def LΔRound(Lf,digital):
    if(str(type(Lf)) in["<class 'float'>"]):
        return round(Lf,digital);
    elif(str(type(Lf)) in["<class 'int'>","<class 'string'>","<class 'bool'>"]):
        return Lf;

    #----浮点列表---------------------------------------------------------------
    L2=[];
    for i,f in enumerate(Lf):
        if(f==1):
            f=1.000;
        L2.append(round(f,digital));
    return L2;

#////end////end////end////end////end////end////end////end////



