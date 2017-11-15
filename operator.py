

import bpy,os,sys
import ctypes
from ctypes import *
from .__init__ import *
from mathutils import Vector
#//Function/////////////////////////////////////////

PI  =3.14159;
piΧ2 = 6.2831;

from .function import*

#////////////////////////////////////////////////
class circleOperator(bpy.types.Operator):
    bl_idname = 'uv.circle'
    bl_label = 'circle '
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "arrange the uv in a precise circle"
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH');
        
    def execute(self, context):
        if(context.scene.tool_settings.use_uv_select_sync== True):
            self.report({"ERROR"},"this addon doesn't work in use_uv_select_sync mode!!!");#"INFO" "ERROR" "DEBUG" "WARNING"
            context.scene.tool_settings.use_uv_select_sync= False;return {'FINISHED'};

        Cmuvl,Liloopcirclecenter=LLLiΔArangeSelectedVers(self);
        if(Cmuvl==None):
            self.report({"ERROR"},"you only select one vertex");
            return {'FINISHED'};

        print("bG",G.bAllclosedselectedversG,G.LlayLLisamelocloop_igroup_ξVerG);
        if(G.bAllclosedselectedversG):
        #if (G.LlayLLisamelocloop_igroup_ξVerG[0][0][1]==G.LlayLLisamelocloop_igroup_ξVerG[0][-1][1]): #全封闭
            uvHead=Cmuvl[ G.LlayLLisamelocloop_igroup_ξVerG[0][0][0][0] ].uv;#[ξVer,[i环选0,-1,i环选2,-1]]
            uvTail=Cmuvl[ G.LlayLLisamelocloop_igroup_ξVerG[0][1][0][0] ].uv;  

        else: #十常点
            #print("i face==",i个面共点);
            uvHead=Cmuvl[ G.LlayLLisamelocloop_igroup_ξVerG[0][0][0][0] ].uv;#[ξVer,[i环选0,i环选2,]]		
            uvTail=Cmuvl[ G.LlayLLisamelocloop_igroup_ξVerG[0][-1][0][0] ].uv;
        
        uv中=Cmuvl[G.LlayLLisamelocloop_igroup_ξVerG[0][len(G.LlayLLisamelocloop_igroup_ξVerG[0])//2][0][0]].uv;
        
        f3XYR=[None,None,None];

        print("HAED",uvHead,"TAIL",uvTail);
        b有圆心=iΔGetCirclecenter_and_radius(uvHead,uvTail,uv中,f3XYR)
        #print("HAEV HART==",b有圆心);
        if(b有圆心==False ):
            
            SmoothUVOperator.execute(self, context);
            bpy.ops.object.mode_set(mode='EDIT');
            self.report({"ERROR"},"There is no center of the circle");#"INFO" "ERROR" "DEBUG" "WARNING"
            return {'FINISHED'};

        fRadius=f3XYR[2];
        f2Circlecenter=[f3XYR[0],f3XYR[1]];

        bClockwise=bΔisClockwise(uvHead,uv中, uvTail, f2Circlecenter);

        fRadianOfOppositeangle=fΔthreepoints_radian(uvHead,uvTail,f2Circlecenter);

        fMiddleradian=fΔthreepoints_radian(uvHead,uvTail,uv中);
        if(fMiddleradian<pi/2):#这是大于半圆的弧●●
            fRadianOfOppositeangle=2*pi-fRadianOfOppositeangle;#取反弧度

        if(G.bAllclosedselectedversG==True):#全封闭
            fRadianOfOppositeangle=-2*pi;

        fRadianOfAverage=fRadianOfOppositeangle/(len(G.LlayLLisamelocloop_igroup_ξVerG[0])-1);
            
        #----赋值uv------------------------------------------------------------------
       #----计算垂直----------------------------------------------
        iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG[0]);
        LvMeshVerCo,LvVerticalVerCo=LLf3ΔGetListOfSelectedVerCo(iNumOfSelectedvers);
        bIsVertical,LfMeshperVerticallength十Add=Lb_LfΔΔGetLenghtOfVerticalMesh(LvVerticalVerCo);
        if(G.bAllclosedselectedversG==True and context.window_manager.bpTransmition):
            for i in range( len(Liloopcirclecenter)):#迭代  此点所有uv loop 赋值圆心
                Cmuvl[Liloopcirclecenter[i]].uv=Vector((f2Circlecenter[0],f2Circlecenter[1]));
            
        iilayer=len(G.LlayLLisamelocloop_igroup_ξVerG);
        iilayerReal=iilayer-1;
        uvRadius乛=uvHead-Vector((f2Circlecenter[0],f2Circlecenter[1]));
        if(not context.window_manager.bpTransmition):
            fProportionPer=fRadiusPer=0;
        else:
            fRadiusPer=fRadius/(iilayerReal);
            fProportionPer=fRadiusPer/uvRadius乛.length;

        for iLay,LLiSamelocloop_igroup_ξVer in enumerate(G.LlayLLisamelocloop_igroup_ξVerG) :
            if(G.bAllclosedselectedversG==False and iLay>0):
                break;
            if(not context.window_manager.bpTransmition and iLay>0):#如果不传播 第貮层就 break;
                break;

            if(iilayer>1 and iLay==iilayer-1):#最后一层不用算，从第貮层算起作第壹层  因为走最后一层时记录了倒数第貮层
                continue;
                
            if(bIsVertical):
                iLengthAdd=len(LfMeshperVerticallength十Add);
                #print("LEN LfLei,Layer==",iLengthAdd,iilayerReal);
                if(LfMeshperVerticallength十Add[iLengthAdd-1]==0):
                    LfMeshperVerticallength十Add[iLengthAdd-1]=0.0000001;bIsVertical=False;
                #print("LEN Lf,Lay-3==",iilayer-3-iLay,iLengthAdd,iilayer-3);
                i=iLengthAdd-1-iLay;
                fProportionThis=LfMeshperVerticallength十Add[i]/LfMeshperVerticallength十Add[iLengthAdd-1];


            for iOrd, LiSamelocloop_igroup_ξVer in enumerate(LLiSamelocloop_igroup_ξVer):
                if (G.bAllclosedselectedversG and (iOrd==0 or iOrd==len(G.LlayLLisamelocloop_igroup_ξVerG[0])-1)): #如果是Head或Tail点 并封闭
                    if(bIsVertical):
                        uvHeadReal=uvRadius乛*fProportionThis+Vector((f2Circlecenter[0],f2Circlecenter[1]));
                    else:
                        uvHeadReal=uvRadius乛-uvRadius乛*fProportionPer*iLay+Vector((f2Circlecenter[0],f2Circlecenter[1]));
                    for i in range( len(LiSamelocloop_igroup_ξVer[0])):#迭代  此点所有uv loop
                        Cmuvl[LiSamelocloop_igroup_ξVer[0][i]].uv=Vector((uvHeadReal[0],uvHeadReal[1]));    
                    continue;
                if(G.bAllclosedselectedversG==False and (iOrd==0 or iOrd==len(G.LlayLLisamelocloop_igroup_ξVerG[0])-1)):#如果 只是线选
                    continue;

                fRadiansPuls十=fRadianOfAverage*iOrd;

                fRadianpuls十2=fΔRadinpuls(uvHead,f2Circlecenter, fRadiansPuls十,bClockwise);

                f2CirclePointReal=[None,None];

                fRadiansPulsReal十=fRadianpuls十2;
                if(bIsVertical):    
                    fRadius=fRadius*fProportionThis;
                    
                else:
                    fRadius=fRadius-(fRadiusPer*iLay);

                Δradian_f2(fRadiansPulsReal十,fRadius, f2Circlecenter,f2CirclePointReal);
                
                for i in range( len(LiSamelocloop_igroup_ξVer[0])):#迭代  此点所有uv loop
                    Cmuvl[LiSamelocloop_igroup_ξVer[0][i]].uv=Vector((f2CirclePointReal[0],f2CirclePointReal[1]));
                
        bpy.ops.object.mode_set(mode='EDIT');
        return {'FINISHED'};

#////////////////////////////////////////////////
class SmoothUVOperator(bpy.types.Operator):
    bl_idname = 'uv.smooth'
    bl_label = 'smooth'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "smooth uv while preserving the shape"

    fDistanceFac=None;
    @classmethod
    def poll(cls, context):
        return True # (context.mode == 'EDIT_MESH');
        
    def execute(self, context):
        if(context.scene.tool_settings.use_uv_select_sync== True):
            self.report({"ERROR"},"this addon doesn't work in use_uv_select_sync mode!!!");#"INFO" "ERROR" "DEBUG" "WARNING"
            context.scene.tool_settings.use_uv_select_sync= False;return {'FINISHED'};

        self.fDistanceFac=G.fDistanceFacG;
        if(self.fDistanceFac==None):
            self.fDistanceFac=context.scene.fpMeshInfulance;
        #----载入数据----------------------------------------------------------------
        id=bpy.context.active_object.data;

        G.LlayLLisamelocloop_igroup_ξVerG=[];
        if(G.bSmooth3G and G.LlayLLisamelocloop_igroup_ξVerG):      
            Cmuvl=CmuvllΔΔGetCmuvll();
        else:
            Cmuvl,Liloopcirclecenter=LLLiΔArangeSelectedVers(self);
            if(Cmuvl==None):
                self.report({"ERROR"},"you only select one vertex");
                return {'FINISHED'};
            #G.LlayLLisamelocloop_igroup_ξVerG=G.LlayLLisamelocloop_igroup_ξVerG;
        #print("G.LlayLLisamelocloop_igroup_ξVerG==",G.LlayLLisamelocloop_igroup_ξVerG);
        #----------------------------------------------------------------------------
        if(G.bAllclosedselectedversG):
            self.report({"ERROR"},"uv line is closed ");#"INFO" "ERROR" "DEBUG" "WARNING"
            return {'FINISHED'};        
        iilayer=len(G.LlayLLisamelocloop_igroup_ξVerG);
        iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG[0]);
        
        LuvSelected=[None]*iNumOfSelectedvers;LuvResult_=[None]*iNumOfSelectedvers;Lf2UVVerticalParallelLine=((c_float*2)*iNumOfSelectedvers)();
  
        for iOrd, LiSamelocloop_igroup_ξVer in enumerate(G.LlayLLisamelocloop_igroup_ξVerG[0]):#第壹层      
            LuvSelected[iOrd]=Cmuvl[LiSamelocloop_igroup_ξVer[0][0]].uv;
        
        LcfPerMeshLength十Add=[0 for f in range(iNumOfSelectedvers)];
        LvMeshVerCo,LvVerticalVerCo=LLf3ΔGetListOfSelectedVerCo(iNumOfSelectedvers);#这个把Cmuvll弄没了

        ΔUVsmooth(LvMeshVerCo,LuvSelected,self.fDistanceFac,LuvResult_);                                                 
        #--赋值给uv------------------------------------------------------------------
        ΔAssignUV(Cmuvl,iNumOfSelectedvers,iilayer,LvVerticalVerCo,LuvResult_,Lf2UVVerticalParallelLine);

        bpy.ops.object.mode_set(mode='EDIT');
        G.fDistanceFacG=None;
        return {'FINISHED'};
        
#////////////////////////////////////////////////     
class Smooth3UVOperator(bpy.types.Operator):
    bl_idname = 'uv.smooth3'
    bl_label = 'smooth'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "smooth uv heavier"
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH');
        
    def execute(self, context):
        G.bSmooth3G=True ;G.LlayLLisamelocloop_igroup_ξVerG=[];

        for fDistanceFac in [0.0,1.0,0.5,bpy.context.scene.fpMeshInfulance]:
            G.fDistanceFacG=fDistanceFac;
            #SmoothUVOperator.execute(self, context);
            bpy.ops.uv.smooth('INVOKE_DEFAULT',);
            print("EXE count",);
        #----------------------------------------------------------------------------
        G.bSmooth3G=False  ;G.LlayLLisamelocloop_igroup_ξVerG=[];
        return {'FINISHED'};
"""
#////SmoothCurve/////////////////////////////////////
class SmoothCurveUVOperator(bpy.types.Operator):
    bl_idname = 'uv.smooth_curve'
    bl_label = 'smooth_curve'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "smooth uv while preserving the shape with curve mathod"

    fDistanceFac=None;
    @classmethod
    def poll(cls, context):
        return True # (context.mode == 'EDIT_MESH');
        
    def execute(self, context):
        if(context.scene.tool_settings.use_uv_select_sync== True):
            self.report({"ERROR"},"this addon doesn't work in use_uv_select_sync mode!!!");#"INFO" "ERROR" "DEBUG" "WARNING"
            context.scene.tool_settings.use_uv_select_sync= False;return {'FINISHED'};

        self.fDistanceFac=G.fDistanceFacG;
        if(self.fDistanceFac==None):
            self.fDistanceFac=context.scene.fpMeshInfulance;
        #----载入数据----------------------------------------------------------------
        id=bpy.context.active_object.data;

        G.LlayLLisamelocloop_igroup_ξVerG=[];
        if(G.bSmooth3G and G.LlayLLisamelocloop_igroup_ξVerG):      
            Cmuvl=CmuvllΔΔGetCmuvll();
        else:
            Cmuvl,Liloopcirclecenter=LLLiΔArangeSelectedVers(self);#LlayLLisamelocloop_igroup_ξVerG ■ 
            if(Cmuvl==None):
                self.report({"ERROR"},"you only select one vertex");
                return {'FINISHED'};
            #G.LlayLLisamelocloop_igroup_ξVerG=G.LlayLLisamelocloop_igroup_ξVerG;
        #print("G.LlayLLisamelocloop_igroup_ξVerG==",G.LlayLLisamelocloop_igroup_ξVerG);
        #----------------------------------------------------------------------------
        if(G.bAllclosedselectedversG):
            self.report({"ERROR"},"uv line is closed ");#"INFO" "ERROR" "DEBUG" "WARNING"
            return {'FINISHED'};        
        iilayer=len(G.LlayLLisamelocloop_igroup_ξVerG);
        iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG[0]);
        
        LuvSelected=[None]*iNumOfSelectedvers;LuvResult_=[None]*iNumOfSelectedvers;Lf2UVVerticalParallelLine=((c_float*2)*iNumOfSelectedvers)();
  
        for iOrd, LiSamelocloop_igroup_ξVer in enumerate(G.LlayLLisamelocloop_igroup_ξVerG[0]):#第壹层      
            LuvSelected[iOrd]=Cmuvl[LiSamelocloop_igroup_ξVer[0][0]].uv;

        LcfPerLength十=[0 for f in range(iNumOfSelectedvers)];LcfPerLength十Add=[0 for f in range(iNumOfSelectedvers)];
        LcfPerMeshLength十Add=[0 for f in range(iNumOfSelectedvers)];
        LvMeshVerCo,LvVerticalVerCo=LLf3ΔGetListOfSelectedVerCo(iNumOfSelectedvers);#这个把Cmuvll弄没了
        
        i共多少曲节=iNumOfSelectedvers*10;
        Δ平均化贝兹重定丅LIB(i共多少曲节,LuvSelected,LuvResult_);
        print("LuvResult_==",LuvResult_);
        #--赋值给uv------------------------------------------------------------------
        ΔAssignUV(Cmuvl,iNumOfSelectedvers,iilayer,LvVerticalVerCo,LuvResult_,Lf2UVVerticalParallelLine);

        bpy.ops.object.mode_set(mode='EDIT');
        G.fDistanceFacG=None;
        return {'FINISHED'};
"""
#////////////////////////////////////////////////
class straightenUVOperator(bpy.types.Operator):
    bl_idname = 'straight.uv'
    bl_label = 'straight'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "straithen uv and homogeneous alignment  "
    bl_register = True
    bl_undo = True
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH');
    def execute(self, context):
        if(context.scene.tool_settings.use_uv_select_sync== True):
            self.report({"ERROR"},"this addon doesn't work in use_uv_select_sync mode!!!");#"INFO" "ERROR" "DEBUG" "WARNING"
            context.scene.tool_settings.use_uv_select_sync= False;return {'FINISHED'};  
        
        Cmuvl,Liloopcirclecenter=LLLiΔArangeSelectedVers(self);
        if(Cmuvl==None):
            self.report({"ERROR"},"you only select one vertex");
            return {'FINISHED'};
        
        if(G.bAllclosedselectedversG):
            self.report({"ERROR"},"selected uv line is closed");#"INFO" "ERROR" "DEBUG" "WARNING"
            print("CLOSE",G.bAllclosedselectedversG);
            return {'FINISHED'};
        #return {'FINISHED'}
        iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG[0]);
        iilayer=len(G.LlayLLisamelocloop_igroup_ξVerG);
        
        uvHead=Cmuvl[G.LlayLLisamelocloop_igroup_ξVerG[0][0][0][0]].uv;	#[ξVer,[i环选0,i环选2,]]		
        uvTail=Cmuvl[G.LlayLLisamelocloop_igroup_ξVerG[0][-1][0][0]].uv;
      
        LuvResult_=[[None,None] for f in range(iNumOfSelectedvers)];Lf2UVVerticalParallelLine=[[None,None] for f in range(iNumOfSelectedvers)];
        #_卐DLL.dll.ΔStraightenUV(iNumOfSelectedvers,f2UVHead,f2UVTail,LuvResult_);  #●●
        LvMeshVerCo,LvVerticalVerCo=LLf3ΔGetListOfSelectedVerCo(iNumOfSelectedvers);
        ΔStraightenUV(iNumOfSelectedvers,uvHead,uvTail,LuvResult_);
  
        ΔAssignUV(Cmuvl,iNumOfSelectedvers,iilayer,LvVerticalVerCo,LuvResult_,Lf2UVVerticalParallelLine);
        if(context.window_manager.bpTransmition and context.window_manager.bpVerticalDistance):
              return bpy.ops.uv.smooth('INVOKE_DEFAULT',);
        bpy.ops.object.mode_set(mode='EDIT');
        return {'FINISHED'}


#///////////////////////////////////////////
class alignUVOperator(bpy.types.Operator):
    bl_idname = 'align.uv'
    bl_label = 'align'
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "align uv in X or Y axis and homogeneous alignment (you can set parameter align to first point or end point later)"
    
    ipLMR=IntProperty(name='LMR',description='left or middle or right',default=1,min=0,max=2,step=1,subtype='NONE',update=None);
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH');
    def invoke(self,context,event):
        self.ipLMR=1;
        #return context.window_manager.invoke_props_dialog(self,400,5def execute(self,context):
        return self.execute(context);
        #return {"FINISHED"};

    def execute(self, context):   
        if(context.scene.tool_settings.use_uv_select_sync== True):
            self.report({"ERROR"},"this addon doesn't work in use_uv_select_sync mode!!!");#"INFO" "ERROR" "DEBUG" "WARNING"
            context.scene.tool_settings.use_uv_select_sync= False;return {'FINISHED'}; 
        Cmuvl,Liloopcirclecenter=LLLiΔArangeSelectedVers(self);
        if(Cmuvl==None):
            self.report({"ERROR"},"you only select one vertex");
            return {'FINISHED'};
        #print("G==",G.bAllclosedselectedversG);
        if(G.bAllclosedselectedversG):
            self.report({"ERROR"},"selected uv line is closed");#"INFO" "ERROR" "DEBUG" "WARNING"
            return {'FINISHED'};
        
        iilayer=len(G.LlayLLisamelocloop_igroup_ξVerG);
        iNumOfSelectedvers=len(G.LlayLLisamelocloop_igroup_ξVerG[0]);
        
        uvHead=Cmuvl[G.LlayLLisamelocloop_igroup_ξVerG[0][0][0][0]].uv;	#[ξVer,[i环选0,i环选2,]]		
        uvTail=Cmuvl[G.LlayLLisamelocloop_igroup_ξVerG[0][-1][0][0]].uv;

        LuvResult_=[[None,None] for f in range(iNumOfSelectedvers)];Lf2UVVerticalParallelLine=[[None,None] for f in range(iNumOfSelectedvers)];

        LvMeshVerCo,LvVerticalVerCo=LLf3ΔGetListOfSelectedVerCo(iNumOfSelectedvers);
        ΔAutoAlignUV(iNumOfSelectedvers,uvHead,uvTail,self.ipLMR,LuvResult_);

        ΔAssignUV(Cmuvl,iNumOfSelectedvers,iilayer,LvVerticalVerCo,LuvResult_,Lf2UVVerticalParallelLine);
        print("EXE==",);
        if(context.window_manager.bpTransmition and context.window_manager.bpVerticalDistance):
            bpy.ops.uv.smooth('INVOKE_DEFAULT',);
        bpy.ops.object.mode_set(mode='EDIT');
        return {'FINISHED'}            
        

class CopyUVOperator(bpy.types.Operator):
    bl_idname = 'copy.uv';
    bl_label = '复制uv';
    bl_options = {'REGISTER', 'UNDO'};   
    bl_description="only the selected uv will be copy"
    
    @classmethod
    def poll(cls, context):      
        return (context.mode == 'EDIT_MESH');
    
    def execute(self, context):
        G.DiSelectedLoopUvG={};
        oA =context.active_object; 
        sOldMode = bpy.context.object.mode 
        bpy.ops.object.mode_set(mode='OBJECT') ;
        Cmuvl =oA.data.uv_layers.active.data ;
        for ξFace,mpAll in enumerate(oA.data.polygons): 
                iFacePoint=len(mpAll.loop_indices);
                for i步3 in range(iFacePoint): 
                    #ξVer = mpAll.vertices[i步3];
                    iLoop=mpAll.loop_indices[i步3];     
                    if(Cmuvl[iLoop].select):#如果 环被选中

                        G.DiSelectedLoopUvG[iLoop]=LΔRound(Cmuvl[iLoop].uv,6);
        
        if (len(G.DiSelectedLoopUvG) == 0): 
            self.report({'WARNING'}, "No faces are not selected.") 
            bpy.ops.object.mode_set(mode=sOldMode) 
            return {'CANCELLED'} 
        else: 
            self.report(  {'INFO'},  "%d ring are selected." % len(G.DiSelectedLoopUvG)) ;

        bpy.ops.object.mode_set(mode=sOldMode) 
         
        return {'FINISHED'} 
        
#----------------------------------------------------------------------------
class PasteUVOperator(bpy.types.Operator):
    bl_idname = 'paste.uv';
    bl_label = 'paste uv';
    bl_options = {'REGISTER', 'UNDO'};    
    
    sp=StringProperty(name="note", description="", default="are you sure paste uv？");
    @classmethod
    def poll(cls, context):      
        return (context.mode == 'EDIT_MESH');
    
    def draw(self, context):
        self.layout.prop(self, "sp");    
    def invoke(self, context, event):#召唤  
        return context.window_manager.invoke_props_dialog(self,400,50);
        
    def execute(self, context): 
        if (G.DiSelectedLoopUvG =={} ): 
        	self.report({'WARNING'}, "Do copy operation at first.");
        	return {'CANCELLED'} 

        oA =context.active_object ;
        id=oA.data;
        sOldMode =context.object.mode ;
        bpy.ops.object.mode_set(mode='OBJECT') 

        CmuvllTarget = oA.data.uv_layers.active.data ;
  
        Di二选环ξ点={};Di二选环Lf2原UVf2后UV={};
        for ξFace,mpAll in enumerate(id.polygons): 
            #if (mpAll.select): #如果 面被选中
                #iFacePoint=len(mpAll.loop_indices);
                Lξ面点=mpAll.vertices;
                for i步, iLoop in enumerate(mpAll.loop_indices):    
                    if(iLoop in G.DiSelectedLoopUvG):
                        if(CmuvllTarget[iLoop].select ):#如果 环被选中
                            if(Di二选环ξ点=={}):
                                Di二选环ξ点[iLoop]=Lξ面点[i步];
                                Di二选环Lf2原UVf2后UV[iLoop]=[];
                                Di二选环Lf2原UVf2后UV[iLoop].append(G.DiSelectedLoopUvG[iLoop]);#{i选环一:[[uv原],]}
                                Di二选环Lf2原UVf2后UV[iLoop].append(CmuvllTarget[iLoop].uv);#{i选环一:[[uv原],[uv后]]}
                            else:
                                #print("RING ",iLoop);
                                if(iLoop not in Di二选环ξ点 and  Lξ面点[i步] not in Di二选环ξ点.values()):#不是同一点ξ里的选环                             
                                    Di二选环ξ点[iLoop]=Lξ面点[i步];
                                    Di二选环Lf2原UVf2后UV[iLoop]=[];
                                    Di二选环Lf2原UVf2后UV[iLoop].append(G.DiSelectedLoopUvG[iLoop]);
                                    Di二选环Lf2原UVf2后UV[iLoop].append(CmuvllTarget[iLoop].uv);#{i选环一:[[uv原],[uv后]],i选环二:[[uv原],[uv后]]}   
                                elif( iLoop in  Di二选环ξ点):
                                    if( Di二选环ξ点[iLoop]!=Lξ面点[i步]):
                                        Di二选环ξ点[iLoop]=Lξ面点[i步];
                                        Di二选环Lf2原UVf2后UV[iLoop]=[];
                                        Di二选环Lf2原UVf2后UV[iLoop].append(G.DiSelectedLoopUvG[iLoop]);
                                        Di二选环Lf2原UVf2后UV[iLoop].append(CmuvllTarget[iLoop].uv);#{i选环一:[[uv原],[uv后]],i选环二:[[uv原],[uv后]]}                          
        #--------------------------------------------------------------------------
        if(Di二选环ξ点!={} and len(Di二选环ξ点)<2):
            self.report({"ERROR"},"must select two points!!");#"INFO" "ERROR" "DEBUG"
            return {'FINISHED'} ;
        #----有选两点--------------------------------------------------------------
        if(Di二选环ξ点 and len(Di二选环ξ点)>1):
            Lf2原一f2后一f2原二f2后二=[];
            for i选环,Lf2原uvf2后uv in Di二选环Lf2原UVf2后UV.items():
                Lf2原一f2后一f2原二f2后二.append(Lf2原uvf2后uv[0]);
                Lf2原一f2后一f2原二f2后二.append(Lf2原uvf2后uv[1]);
                
            f2原uv一=Lf2原一f2后一f2原二f2后二[0];f2后uv一=Lf2原一f2后一f2原二f2后二[1];
            
            f2乛原=f2一f2(Lf2原一f2后一f2原二f2后二[2],f2原uv一);
            f2乛后=f2一f2(Lf2原一f2后一f2原二f2后二[3],f2后uv一);
            f逆转弧=fΔReverseRadians十(f2乛原, f2乛后);
            #----求比例---------------------------------------------------------------
            f线Length原=sqrt(pow(f2乛原[0],2)+pow(f2乛原[1],2));
            f线Length后=sqrt(pow(f2乛后[0],2)+pow(f2乛后[1],2));
            f比例=f线Length后/f线Length原;
            #----赋值 uv ----------------------------------------------------------------
            for iLoop,UV  in G.DiSelectedLoopUvG.items(): 
                f2乛原当前=f2一f2(UV,f2原uv一);#把f2原uv一 当圆心
                f2OldTurn=f2ΔReverseRadiansVector(f2乛原当前, f逆转弧);
                #print("TURN ==",f逆转弧,f2乛原当前,f2OldTurn);
                uvReal=f2十f2([f2OldTurn[0]*f比例,f2OldTurn[1]*f比例],f2后uv一);#丅移动到f2后uv一
                CmuvllTarget[iLoop].uv=uvReal;
                
        #----无选点-----------------------------------------------------------------
        else:
            for iLoop,UV  in G.DiSelectedLoopUvG.items(): 
                CmuvllTarget[iLoop].uv=UV;

        self.report(  {'INFO'},  "%d indices are pasted." % len(CmuvllTarget));

        bpy.ops.object.mode_set(mode=sOldMode) 

        return {'FINISHED'} 
        
   
#////////////////////////////////////////////////
class 卐Panel(bpy.types.Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_idname = 'smoothuv'
    bl_label = "uv_tools"
    bl_context = "objectmode"
    #bpy.types.UVLoopLayers.fp参数uvll=FloatProperty(name="fpMeshInfulance", description="--", default=0.0, min=0.0, max=1.0, soft_min=0.0, soft_max=1.0, step=3, precision=2)
    #bl_options = {'DEFAULT_CLOSED'}
    def draw(self, context):
        uil = self.layout
        uilC1= uil.column(align=True)
        uilC=uilC1.split(0.2)
        uilC.operator(circleOperator.bl_idname, text="Circle",icon="SPHERECURVE")
        uilC.operator(SmoothUVOperator.bl_idname, text="Smooth",icon="SMOOTHCURVE")
        #uilC.operator(SmoothCurveUVOperator.bl_idname, text="smooth curve")
        uilC.operator(Smooth3UVOperator.bl_idname, text="smooth*3")
        uilR=uil.row(align=True);
        uilR.prop( context.scene, "fpMeshInfulance", text = "mesh influence", slider = True,translate=True);
        uilR=uil.row(align=True);
        uilR.prop( context.window_manager, "bpTransmition", text = "transmission", toggle=True);
        uilR.prop( context.window_manager, "bpVerticalDistance", text = "vertical", toggle=True);
        uilR.prop( context.window_manager, "bpXYwm", text = "XY", toggle=False);
        #uil.separator();
        uilC=uil.column(align=True).split(0.5);
        uilC.operator(straightenUVOperator.bl_idname, text="Straighten",icon="LINCURVE");
        uilC.operator(alignUVOperator.bl_idname, text="Align",icon="NOCURVE");
        
        uil.separator();
        uilC=uil.column(align=True).split(0.3);
        uilC.operator(CopyUVOperator.bl_idname, text="copy  selected uv",icon="COPYDOWN") ;
        uilC.operator(PasteUVOperator.bl_idname, text="paste uv",icon="PASTEDOWN") ;
        #uilC.operator(卐关于我卐Operator.bl_idname, text="about me",icon="QUESTION") ;



#////end////end////end////end////end////end////end////end////






