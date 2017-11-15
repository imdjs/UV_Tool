

import bpy,sys,os,imp,random

from bpy.props import *
from mathutils import Matrix,Vector,Euler
from ctypes import*
from bpy_extras import object_utils
import bmesh
from math import*

#from .PYLIB_math_curve import*
#////////////////////////////////////////////////
piΞ2=pi/2;
piΧ2=pi*2;

#////////////////////////////////////////////////    
 
#--------数学公式--------------------------------------------------------------------------
def  atan3(x, y):#求出360度内正Radian度  
    z=pow(x,2)+pow(y,2);
    if(z==0):
        return 0;
        #z==0.00001;
        
    if(y>=0 ):#在↑
        return acos(x/sqrt(z));
    else:#(y<0and x<=0)#在↙    
        #print("y<=0\n");
        c=acos(x/sqrt(z));
        return c+(pi-c)*2;
        
def f2十f2(f2一,  f2二):   return [f2一[0]+f2二[0],f2一[1]+f2二[1]];
def f2十f2_f2(f2一,  f2二,f2三):  f2三[0]=f2一[0]+f2二[0];f2三[1]=f2一[1]+f2二[1];
def f3十f3(vMinus,  f3二):   return [vMinus[0]+f3二[0],vMinus[1]+f3二[1],vMinus[2]+f3二[2]];
def f3十f3_f3(vMinus,  f3二,f3三):   f3三[0]=vMinus[0]+f3二[0];f3三[1]=vMinus[1]+f3二[1];f3三[2]=vMinus[2]+f3二[2];

def f2一f2(f2一,  f2二):   return [f2一[0]-f2二[0],f2一[1]-f2二[1]];
def f3一f3(vMinus,  f3二):   return [vMinus[0]-f3二[0],vMinus[1]-f3二[1],vMinus[2]-f3二[2]];


def LengthF2(f2一,  f2二):   
    f2三=[None,None];f2三[0]=f2一[0]-f2二[0];f2三[1]=f2一[1]-f2二[1];
    fUVDistance=sqrt(pow(f2三[0],2)+pow(f2三[1],2));
    return fUVDistance;
    
def LengthF3(vMinus,  f3二):
    f3Length=[None,None,None];f3Length[0]=vMinus[0]-f3二[0];f3Length[1]=vMinus[1]-f3二[1];f3Length[2]=vMinus[2]-f3二[2];
    fOppAngleLineLength=sqrt(pow(f3Length[0],2)+pow(f3Length[1],2)+pow(f3Length[2],2));
    return fOppAngleLineLength;

def f2一f2_f2(f2一,  f2二,f2三):f2三[0]=f2一[0]-f2二[0];f2三[1]=f2一[1]-f2二[1];
    
def f3一f3_f3(vMinus,  f3二,  f3三): f3三[0]=vMinus[0]-f3二[0];f3三[1]=vMinus[1]-f3二[1];f3三[2]=vMinus[2]-f3二[2];
   
def f2Χf_f2(vMinus,  f,  f2三): f2三[0]=vMinus[0]*f;f2三[1]=vMinus[1]*f;
def f3Χf_f3(vMinus,  f,  f2三): f2三[0]=vMinus[0]*f;f2三[1]=vMinus[1]*f;f2三[2]=vMinus[2]*f;
def f3Χf(vMinus,  f): return [vMinus[0]*f,vMinus[1]*f,vMinus[2]*f];

def Cos(v壹,v二):
    v此=v壹.normalized();v2=v二.normalized();#一定要分开

    fLengthProject=v此.dot(v2);#如果其中一EdgeLength为零,就当它是90度,极少出现

    if(fLengthProject<-1.0):fLengthProject=-1.0;
    elif(fLengthProject>1.0):fLengthProject=1.0;#●●防止__出现 -1.#IND00
    
    return fLengthProject;
    
def tSum(f3):
    艹=0;
    for t in f3:
        艹+=t;
    return 艹;

#==============================================================
def fΔReverseRadians十(f2Ver一, f2Ver二):#这个Angle可以大于180度
    fOppRadian一=atan3(f2Ver一[0],f2Ver一[1]);#  Y#X
    fOppRadian二=atan3(f2Ver二[0],f2Ver二[1]);
    if(fOppRadian一<fOppRadian二):
        return fOppRadian二-fOppRadian一;
    elif(fOppRadian一>fOppRadian二):
        return 360-(fOppRadian一-fOppRadian二);
    elif(fOppRadian一==fOppRadian二):
        return 0.0;

def f2ΔReverseRadiansVector(f2Ver一, f逆转Radian度):#这个Angle可以大于180度
    fRadian一=atan3(f2Ver一[0],f2Ver一[1]);#  Y#X
    f最终Radian=(fRadian一+f逆转Radian度)%piΧ2;
    fLineLength=sqrt(pow(f2Ver一[0],2)+pow(f2Ver一[1],2));
    
    f2结果=[None,None];
    f2结果[0]=fLineLength*cos(f最终Radian);f2结果[1]=fLineLength*sin(f最终Radian);
    return f2结果;
    
def fΔRadianOfAngleF2(f2Ver一, f2Ver二):#这个夹Angle是小于180度
    # f2Circlecenter=0.0f,0.0f; f2Head
    fOppRadian一=atan3(f2Ver一[0],f2Ver一[1]);#  Y#X
    fOppRadian二=atan3(f2Ver二[0],f2Ver二[1]);
    return abs(fOppRadian二-fOppRadian一);    
    
def fΔRadianOfAngleF3(f3Ver一, f3Ver二):#这个夹Angle是小于180度 正
    #double c, d;
    c = f3Ver一[0]*f3Ver二[0] + f3Ver一[1]*f3Ver二[1] + f3Ver一[2]*f3Ver二[2];#Ver积
    d = sqrt(f3Ver一[0]*f3Ver一[0] + f3Ver一[1]*f3Ver一[1] + f3Ver一[2]*f3Ver一[2]) * sqrt(f3Ver二[0]*f3Ver二[0] + f3Ver二[1]*f3Ver二[1] + f3Ver二[2]*f3Ver二[2]);#这两个乛Length相乘
    if(d==0):d=0.0001;
    #print("ACOS==",acos(c/d));
    return acos(c/d); 


def fΔGetVectorOfAngle(f2SideEdge乛, f2斜Edge乛, f2OppEdge乛__):#求OppEdge的乛
    fRadianAangle=fΔRadianOfAngleF2(f2SideEdge乛,f2斜Edge乛);
    fSideEdgeLength=sqrt(pow(f2SideEdge乛[0],2)+pow(f2SideEdge乛[1],2));#length
    ftiltEdgeLength=sqrt(pow(f2斜Edge乛[0],2)+pow(f2斜Edge乛[1],2));
    fOppEdgeLength=ftiltEdgeLength*cos(fRadianAangle);
    fSideEdgeProportion=fOppEdgeLength/fSideEdgeLength;
    f2OppEdge乛__[0]=f2SideEdge乛[0]*fSideEdgeProportion;f2OppEdge乛__[1]=f2SideEdge乛[1]*fSideEdgeProportion;
#☐☐/┃☐☐☐☐
#☐/☐↓☐☐☐☐☐☐
#☐━━☐☐☐☐☐☐☐

#///////////////////////////////////////////
def LΔΔ保留4丅小数(Lf):
    if(str(type(Lf)) in["<class 'float'>"]):
        return round(Lf,4);
    elif(str(type(Lf)) in["<class 'int'>","<class 'string'>","<class 'bool'>"]):
        return Lf;

    #----列表浮Ver---------------------------------------------------------------
    L2=[];
    for i,f in enumerate(Lf):
        if(f==1):
            f=1.000;
        L2.append(round(f,4));
    return L2;
#///////////////////////////////////////////
def LΔRound(Lf,i小数丅):
    if(str(type(Lf)) in["<class 'float'>"]):
        return round(Lf,i小数丅);
    elif(str(type(Lf)) in["<class 'int'>","<class 'string'>","<class 'bool'>"]):
        return Lf;

    #----浮Ver列表---------------------------------------------------------------
    L2=[];
    for i,f in enumerate(Lf):
        if(f==1):
            f=1.000;
        L2.append(round(f,i小数丅));
    return L2;
#////曲Line//////////////////////////////////////








#///end////end////end////end////end////end////end////end////end////



