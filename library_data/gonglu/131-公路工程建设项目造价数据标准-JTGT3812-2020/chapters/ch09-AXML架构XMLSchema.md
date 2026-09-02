# 章 附录A:A XML 架构（XML Schema）
# 规范: (131-公路工程建设项目造价数据标准-JTGT3812-2020) | 页码:PDF 114-255
# 条文范围:-
# 类型:正文
# 生成:spec.py index 2026-08-26 | 页内标记【第 N 页】用于回源

【第 114 页】
XML 架构（XMLSchema） 
‐ 107 ‐ 
附录A XML 架构（XML Schema） 
A.0.1 造价依据数据XML Schema 
<?xml version="1.0" encoding="UTF-8" ?> 
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
<xs:complexType name="BaseType"> 
<xs:annotation> 
<xs:documentation>基类元素</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="CustomData" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>自定义数据</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:attribute name="Id" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据内部编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DataName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DataValue" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PId" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>父结点ID</xs:documentation> 
</xs:annotation>

【第 115 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 108 ‐ 
</xs:attribute> 
</xs:complexType> 
</xs:element> 
</xs:sequence>    
<xs:attribute name="KeyId" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>实体主键</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:complexType> 
<xs:complexType name="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="LibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LibName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ShortName" type="xs:string"> 
<xs:annotation> 
<xs:documentation>造价依据简称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CheckCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>校验码</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 116 页】
XML 架构（XMLSchema） 
‐ 109 ‐ 
<xs:attribute name="ReleaseDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>发布日期</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>标准名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Version" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>标准版本</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MakeDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>文件生成时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:complexType name="PractBase"> 
<xs:annotation> 
<xs:documentation>工料机库基类</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Uuid" type="xs:string" use="required"> 
<xs:annotation>

【第 117 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 110 ‐ 
<xs:documentation>工料机唯一编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Spec" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机规格</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="NormPrice" type="xs:double"> 
<xs:annotation> 
<xs:documentation>工料机基价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:complexType name="DirectoryBase"> 
<xs:annotation> 
<xs:documentation>定额章节表基类</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Item" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>定额子目</xs:documentation>

【第 118 页】
XML 架构（XMLSchema） 
‐ 111 ‐ 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Consume" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>定额消耗</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Consumption" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>工料机消耗量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Uuid" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目唯一编码</xs:documentation> 
</xs:annotation>

【第 119 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 112 ‐ 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目基价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:sequence> 
<xs:element name="Directorys" maxOccurs="unbounded" minOccurs="0" type="DirectoryBase"> 
<xs:annotation> 
<xs:documentation>定额章节表</xs:documentation> 
</xs:annotation> 
</xs:element> 
</xs:sequence> 
</xs:sequence> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>章节表编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>章节表名称</xs:documentation>

【第 120 页】
XML 架构（XMLSchema） 
‐ 113 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Content" type="xs:string"> 
<xs:annotation> 
<xs:documentation>章节说明及工程内容</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:complexType name="StandardItemsBase"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)表</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="StandardItems" type="StandardItemsBase"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)表</xs:documentation> 
</xs:annotation> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="ItemCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ItemName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)名称</xs:documentation>

【第 121 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 114 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MeterRules" type="xs:string"> 
<xs:annotation> 
<xs:documentation>计量规则</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Content" type="xs:string"> 
<xs:annotation> 
<xs:documentation>工作内容</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:element name="BasicFile"> 
<xs:annotation> 
<xs:documentation>造价依据</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="NormFile" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>定额资源</xs:documentation>

【第 122 页】
XML 架构（XMLSchema） 
‐ 115 ‐ 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="NormLib" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>定额库</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="Directorys" maxOccurs="unbounded" minOccurs="1" type="DirectoryBase"> 
<xs:annotation> 
<xs:documentation>定额章节表目录</xs:documentation> 
</xs:annotation> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="PractlibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（工料机）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="PractLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>工料机库</xs:documentation> 
</xs:annotation> 
<xs:complexType>

【第 123 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 116 ‐ 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="Mps" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>人工</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Mp" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>人工明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="PractBase"> 
<xs:annotation> 
<xs:documentation>工料(设备)机库基类</xs:documentation> 
</xs:annotation> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Materials" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>材料</xs:documentation>

【第 124 页】
XML 架构（XMLSchema） 
‐ 117 ‐ 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Material" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>材料明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="PractBase"> 
<xs:annotation> 
<xs:documentation>工料(设备)机库基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="GwRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单位毛重</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OffSiteLf" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>场外运输损耗率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OnSiteLf" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>场内运输损耗率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LoadLf" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>每增加1 次装卸损耗率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="StoreRate" type="xs:double" use="required">

【第 125 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 118 ‐ 
<xs:annotation> 
<xs:documentation>采购及保管费率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PackageRecycleFee" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>包装回收费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Mechs" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>机械</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Mech" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>机械台班定额</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="PractBase"> 
<xs:annotation> 
<xs:documentation>工料(设备)机库基类</xs:documentation> 
</xs:annotation>

【第 126 页】
XML 架构（XMLSchema） 
‐ 119 ‐ 
<xs:sequence> 
<xs:element name="FixedCost" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>不变费用</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="FixedCostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>不变费用明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="FixedCostNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>不变费用明细编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="VariableCost" maxOccurs="1" minOccurs="1">

【第 127 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 120 ‐ 
<xs:annotation> 
<xs:documentation>可变费用</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="VariableCostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>可变费用消耗明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="VariableCostNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>可变费用消耗明细编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Consumption" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>消耗量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent>

【第 128 页】
XML 架构（XMLSchema） 
‐ 121 ‐ 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="RateLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>费率标准库</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="CostTypes" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>工程类别</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence>

【第 129 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 122 ‐ 
<xs:element name="CostType" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>工程类别明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="RateTypes" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率类别</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="RateType" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率类别明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType">

【第 130 页】
XML 架构（XMLSchema） 
‐ 123 ‐ 
<xs:attribute name="RateTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="RateValues" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率值</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="RateValue" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率值明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateTypeNo" type="xs:string" use="required"> 
<xs:annotation>

【第 131 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 124 ‐ 
<xs:documentation>费率类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateParamNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率参数编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateValue" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>费率值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="ItemStandardLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)表库</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation>

【第 132 页】
XML 架构（XMLSchema） 
‐ 125 ‐ 
</xs:annotation> 
<xs:sequence> 
<xs:element name="StandardItems" type="StandardItemsBase"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)表</xs:documentation> 
</xs:annotation> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="TaxLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>车船税费库</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="TaxItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>车船税费明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="UseTax" type="xs:double">

【第 133 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 126 ‐ 
<xs:annotation> 
<xs:documentation>车船税(元/t·年)</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="UseTaxTon" type="xs:double"> 
<xs:annotation> 
<xs:documentation>车船税计量吨</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MonthPerYear" type="xs:double"> 
<xs:annotation> 
<xs:documentation>年工作月</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DayPerYear" type="xs:double"> 
<xs:annotation> 
<xs:documentation>年工作台班</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxAmount" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>车船税合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="PractlibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（工料机）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent>

【第 134 页】
XML 架构（XMLSchema） 
‐ 127 ‐ 
</xs:complexType> 
</xs:element> 
<xs:element name="PriceLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>价格信息</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="Material" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>材料价格明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxPrice" type="xs:double"> 
<xs:annotation> 
<xs:documentation>原价（不含税）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PriceType" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>价格类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string">

【第 135 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 128 ‐ 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="PractlibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（工料机）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="MpPriceLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>人工单价</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="MpPrice"> 
<xs:annotation> 
<xs:documentation>人工单价明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType">

【第 136 页】
XML 架构（XMLSchema） 
‐ 129 ‐ 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>价格</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Area" type="xs:string"> 
<xs:annotation> 
<xs:documentation>地区描述</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="PractlibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（工料机）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="FeeRateLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>规费费率</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase">

【第 137 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 130 ‐ 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="FeeRates"> 
<xs:annotation> 
<xs:documentation>规费费率明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别编码（规费）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别名称（规费）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="value" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>费率值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence>

【第 138 页】
XML 架构（XMLSchema） 
‐ 131 ‐ 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="ProfitRateLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>利润率</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="ProfitRates"> 
<xs:annotation> 
<xs:documentation>利润率明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别编码（利润率）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="value" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>利润率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation>

【第 139 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 132 ‐ 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="TaxRateLib" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>税率</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="LibBase"> 
<xs:annotation> 
<xs:documentation>造价依据基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="TaxRates"> 
<xs:annotation> 
<xs:documentation>税率明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别编码（税率）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxValue" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>税率</xs:documentation>

【第 140 页】
XML 架构（XMLSchema） 
‐ 133 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:schema> 
A.0.2 估概预算（清单）造价成果数据XML Schema 
<?xml version="1.0" encoding="UTF-8" ?> 
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
<xs:complexType name="BaseType"> 
<xs:annotation> 
<xs:documentation>基类元素</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="CustomData" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>自定义数据</xs:documentation> 
</xs:annotation> 
<xs:complexType>

【第 141 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 134 ‐ 
<xs:attribute name="Id" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据内部编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DataName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DataValue" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PId" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>父结点ID</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:complexType> 
</xs:element> 
</xs:sequence>    
<xs:attribute name="KeyId" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>实体主键</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:complexType> 
<xs:complexType name="PractBase"> 
<xs:annotation> 
<xs:documentation>工料机单价文件基类</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required">

【第 142 页】
XML 架构（XMLSchema） 
‐ 135 ‐ 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PractName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Spec" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机规格</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="BudgetPrice" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>预算单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="NormPrice" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>工料机基价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="BudgetSum" type="xs:double" use="required"> 
<xs:annotation>

【第 143 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 136 ‐ 
<xs:documentation>预算金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="NormSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>定额金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="IsAdd" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>补充工料机</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:complexType name="ItemBase"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）表基类</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostComposition" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）组价</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Formula" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>算式列表</xs:documentation> 
</xs:annotation> 
<xs:complexType>

【第 144 页】
XML 架构（XMLSchema） 
‐ 137 ‐ 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>名称/描述</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Formulas" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>计算式</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Ratio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Cost" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>费用列表</xs:documentation> 
</xs:annotation> 
<xs:complexType>

【第 145 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 138 ‐ 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:annotation> 
<xs:documentation>费用构成明细</xs:documentation> 
</xs:annotation> 
<xs:element name="CostStructure" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用构成明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="ItemNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费用明细编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>明细金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence>

【第 146 页】
XML 架构（XMLSchema） 
‐ 139 ‐ 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>名称/描述</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Spec" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>规格</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="BasePrice" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>基价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required">

【第 147 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 140 ‐ 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="IsEquipment" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>是否设备：0=否；1=是；</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProfitRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>利润率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>税率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MpRatio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>人工费比例</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MaterialRatio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>材料费比例</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MechRatio" type="xs:double"> 
<xs:annotation>

【第 148 页】
XML 架构（XMLSchema） 
‐ 141 ‐ 
<xs:documentation>机械费比例</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Norm" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>定额列表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostStructure" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用构成明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="ItemNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费用明细编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required">

【第 149 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 142 ‐ 
<xs:annotation> 
<xs:documentation>明细金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Consume" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>定额消耗</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="ConsumeItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>定额消耗明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Consumption" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>消耗量</xs:documentation>

【第 150 页】
XML 架构（XMLSchema） 
‐ 143 ‐ 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="NormLibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（定额指标）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DisplayCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>定额数量</xs:documentation> 
</xs:annotation>

【第 151 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 144 ‐ 
</xs:attribute> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProfitRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>利润率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>税率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="FabricationCost" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AdjustStatus" type="xs:string"> 
<xs:annotation> 
<xs:documentation>调整状态</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<!--

【第 152 页】
XML 架构（XMLSchema） 
‐ 145 ‐ 
费用构成明细 
--> 
<xs:element name="CostStructure" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用构成明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="ItemNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费用明细编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>明细金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element>

【第 153 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 146 ‐ 
<xs:sequence> 
<xs:element name="Item" maxOccurs="unbounded" minOccurs="0" type="ItemBase"> 
<xs:annotation> 
<xs:documentation>要素费用项目(清单)表</xs:documentation> 
</xs:annotation> 
</xs:element> 
</xs:sequence> 
</xs:sequence> 
<xs:attribute name="ListCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ListName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit1" type="xs:string"> 
<xs:annotation> 
<xs:documentation>单位1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit2" type="xs:string"> 
<xs:annotation> 
<xs:documentation>单位2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation>

【第 154 页】
XML 架构（XMLSchema） 
‐ 147 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num1" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProvisionalType" type="xs:integer"> 
<xs:annotation> 
<xs:documentation>暂估价类型</xs:documentation> 
</xs:annotation>

【第 155 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 148 ‐ 
</xs:attribute> 
<xs:attribute name="MeterRules" type="xs:string"> 
<xs:annotation> 
<xs:documentation>计量规则</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Content" type="xs:string"> 
<xs:annotation> 
<xs:documentation>工程内容</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MpRatio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>人工调价系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MaterialRatio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>材料调价系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MechRatio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>机械调价系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AdjustedPrice" type="xs:double"> 
<xs:annotation> 
<xs:documentation>调价后单价</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 156 页】
XML 架构（XMLSchema） 
‐ 149 ‐ 
<xs:attribute name="AdjustedSums" type="xs:double"> 
<xs:annotation> 
<xs:documentation>调价后合价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ItemType" type="xs:integer"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="FormulaCode" type="xs:string"> 
<xs:annotation> 
<xs:documentation>计算式编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:element name="CprjInfo"> 
<xs:annotation> 
<xs:documentation>建设项目</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="SystemInfo" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>基本信息</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>标准名称</xs:documentation>

【第 157 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 150 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Version" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>标准版本</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SoftwareName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>软件名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SoftwareVer" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>软件版本</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SoftwareCompany" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>软件公司名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MakeDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>文件生成时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MacAddress" type="xs:string"> 
<xs:annotation> 
<xs:documentation>网卡地址</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="HardNumber" type="xs:string"> 
<xs:annotation> 
<xs:documentation>硬盘序列号</xs:documentation> 
</xs:annotation>

【第 158 页】
XML 架构（XMLSchema） 
‐ 151 ‐ 
</xs:attribute> 
<xs:attribute name="SoftwareNumber" type="xs:string"> 
<xs:annotation> 
<xs:documentation>软件序列号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="CostBasis" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>造价依据</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="NormLib" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>定额库</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="NormLibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（定额指标）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="NormLibName" type="xs:string"> 
<xs:annotation> 
<xs:documentation>造价依据名称（定额指标）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Type" type="xs:string" use="required">

【第 159 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 152 ‐ 
<xs:annotation> 
<xs:documentation>定额库类型编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="MakeRuleNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（编制办法）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MakeRuleName" type="xs:string"> 
<xs:annotation> 
<xs:documentation>造价依据名称（编制办法）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ItemStandardNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（要素费用项目）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Rate" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率文件</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence>

【第 160 页】
XML 架构（XMLSchema） 
‐ 153 ‐ 
<xs:element name="RateParams" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>取费参数</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="RateParam" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>取费参数明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="RateTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateParamNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别取值参数编码或值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Ratio" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>比例</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension>

【第 161 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 154 ‐ 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="RateValues" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率值</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="RateValue" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费率值明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateValue" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>费率值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType>

【第 162 页】
XML 架构（XMLSchema） 
‐ 155 ‐ 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="RateNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率文件编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率文件名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateLibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（费率）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Pract" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>工料机单价文件</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Mps" maxOccurs="1" minOccurs="1"> 
<xs:annotation>

【第 163 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 156 ‐ 
<xs:documentation>人工</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Mp" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>人工明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="PractBase"> 
<xs:annotation> 
<xs:documentation>工料（设备）机单价基类</xs:documentation> 
</xs:annotation> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Materials" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>材料</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Material" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>材料明细</xs:documentation>

【第 164 页】
XML 架构（XMLSchema） 
‐ 157 ‐ 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="PractBase"> 
<xs:annotation> 
<xs:documentation>工料（设备）机单价基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="Electro" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>综合电价构成</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>供电编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>电单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Ratio" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>比例</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="OrgPrices" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation>

【第 165 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 158 ‐ 
<xs:documentation>原价（不含税）</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="SelfCollect" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>材料自采</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Norm" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>定额列表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostStructure" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用构成明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
  <xs:extension base="BaseType"> 
 
<xs:sequence> 
 
   <xs:element name="CostItem" maxOccurs="unbounded" minOccurs="1"> 
 
 
  <xs:annotation> 
 
 
 
 <xs:documentation>费用明细</xs:documentation> 
 
 
  </xs:annotation> 
 
 
  <xs:complexType> 
 
 
 
 <xs:complexContent>

【第 166 页】
XML 架构（XMLSchema） 
‐ 159 ‐ 
 
 
 
 
<xs:extension base="BaseType"> 
 
 
 
 
  <xs:attribute name="ItemNo" type="xs:string" use="required"> 
 
 
 
 
 
 <xs:annotation> 
 
 
 
 
 
 
<xs:documentation>费用明细编码</xs:documentation> 
 
 
 
 
 
 </xs:annotation> 
 
 
 
 
  </xs:attribute> 
 
 
 
 
  <xs:attribute name="Sum" type="xs:double" use="required"> 
 
 
 
 
 
 <xs:annotation> 
 
 
 
 
 
 
<xs:documentation>明细金额</xs:documentation> 
 
 
 
 
 
 </xs:annotation> 
 
 
 
 
  </xs:attribute> 
 
 
 
 
</xs:extension> 
 
 
 
 </xs:complexContent> 
 
 
  </xs:complexType> 
 
   </xs:element> 
 
</xs:sequence> 
  </xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Consume"> 
<xs:annotation> 
<xs:documentation>定额消耗</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
  <xs:extension base="BaseType"> 
 
<xs:sequence> 
 
   <xs:element name="ConsumeItem" maxOccurs="unbounded" minOccurs="1"> 
 
 
  <xs:annotation> 
 
 
 
 <xs:documentation>定额消耗明细</xs:documentation> 
 
 
  </xs:annotation> 
 
 
  <xs:complexType> 
 
 
 
 <xs:complexContent> 
 
 
 
 
<xs:extension base="BaseType"> 
 
 
 
 
  <xs:attribute name="Code" type="xs:string" use="required">

【第 167 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 160 ‐ 
 
 
 
 
 
 <xs:annotation> 
 
 
 
 
 
 
<xs:documentation>工料机编码</xs:documentation> 
 
 
 
 
 
 </xs:annotation> 
 
 
 
 
  </xs:attribute> 
 
 
 
 
  <xs:attribute name="Consumption" type="xs:double" use="required"> 
 
 
 
 
 
 <xs:annotation> 
 
 
 
 
 
 
<xs:documentation>消耗量</xs:documentation> 
 
 
 
 
 
 </xs:annotation> 
 
 
 
 
  </xs:attribute> 
 
 
 
 
</xs:extension> 
 
 
 
 </xs:complexContent> 
 
 
  </xs:complexType> 
 
   </xs:element> 
 
</xs:sequence> 
  </xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="NormLibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（定额指标）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DisplayCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation>

【第 168 页】
XML 架构（XMLSchema） 
‐ 161 ‐ 
<xs:documentation>定额子目单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>定额数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProfitRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>利润率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>税率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="FabricationCost" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AdjustStatus" type="xs:string"> 
<xs:annotation> 
<xs:documentation>调整状态</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType>

【第 169 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 162 ‐ 
</xs:element> 
</xs:sequence> 
<xs:attribute name="OtherCost" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>其它费用</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="OrgPricevalue" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>原价（不含税）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Ratio" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>自采比例</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="TransFees" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>运杂费</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:sequence> 
<xs:element name="SelfTrans" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>自办运输</xs:documentation> 
</xs:annotation>

【第 170 页】
XML 架构（XMLSchema） 
‐ 163 ‐ 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Norm" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>定额列表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CostStructure" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用构成明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
  <xs:element name="CostItem" maxOccurs="unbounded" minOccurs="1"> 
 
 <xs:annotation> 
 
 
<xs:documentation>费用明细</xs:documentation> 
 
 </xs:annotation> 
 
 <xs:complexType> 
 
 
<xs:complexContent> 
 
 
   <xs:extension base="BaseType"> 
 
 
 
 <xs:attribute name="ItemNo" type="xs:string" use="required"> 
 
 
 
 
<xs:annotation> 
 
 
 
 
   <xs:documentation>费用明细编码</xs:documentation> 
 
 
 
 
</xs:annotation> 
 
 
 
 </xs:attribute> 
 
 
 
 <xs:attribute name="Sum" type="xs:double" use="required"> 
 
 
 
 
<xs:annotation> 
 
 
 
 
   <xs:documentation>明细金额</xs:documentation> 
 
 
 
 
</xs:annotation>

【第 171 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 164 ‐ 
 
 
 
 </xs:attribute> 
 
 
   </xs:extension> 
 
 
</xs:complexContent> 
 
 </xs:complexType> 
  </xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Consume"> 
<xs:annotation> 
<xs:documentation>定额消耗</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
  <xs:element name="ConsumeItem" maxOccurs="unbounded" minOccurs="1"> 
 
 <xs:annotation> 
 
 
<xs:documentation>定额消耗明细</xs:documentation> 
 
 </xs:annotation> 
 
 <xs:complexType> 
 
 
<xs:complexContent> 
 
 
   <xs:extension base="BaseType"> 
 
 
 
 <xs:attribute name="Code" type="xs:string" use="required"> 
 
 
 
 
<xs:annotation> 
 
 
 
 
   <xs:documentation>工料机编码</xs:documentation> 
 
 
 
 
</xs:annotation> 
 
 
 
 </xs:attribute> 
 
 
 
 <xs:attribute name="Consumption" type="xs:double" use="required"> 
 
 
 
 
<xs:annotation> 
 
 
 
 
   <xs:documentation>消耗量</xs:documentation> 
 
 
 
 
</xs:annotation> 
 
 
 
 </xs:attribute> 
 
 
   </xs:extension>

【第 172 页】
XML 架构（XMLSchema） 
‐ 165 ‐ 
 
 
</xs:complexContent> 
 
 </xs:complexType> 
  </xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="NormLibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（定额指标）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DisplayCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>定额子目单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>定额数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CostTypeNo" type="xs:string" use="required"> 
<xs:annotation>

【第 173 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 166 ‐ 
<xs:documentation>工程类别编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProfitRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>利润率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>税率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="FabricationCost" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AdjustStatus" type="xs:string"> 
<xs:annotation> 
<xs:documentation>调整状态</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="FromPlace" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>起讫点</xs:documentation>

【第 174 页】
XML 架构（XMLSchema） 
‐ 167 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TransWay" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>运输方式</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TransDistence" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>运距</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TransFee" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>吨·公里运价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LoadTimes" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>装卸次数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LoadCost" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>装卸单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OtherCost" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>其它费用</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Ratio" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>加权系数</xs:documentation> 
</xs:annotation>

【第 175 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 168 ‐ 
</xs:attribute> 
<xs:attribute name="Freight" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单位运费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="OrgPrice" type="xs:double"> 
<xs:annotation> 
<xs:documentation>原价（不含税价）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TransFee" type="xs:double"> 
<xs:annotation> 
<xs:documentation>运杂费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="GwRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单位毛重</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OffSiteLf" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>场外运输损耗率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OnSiteLf" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>场内运输损耗费率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LoadLf" type="xs:double" use="required"> 
<xs:annotation>

【第 176 页】
XML 架构（XMLSchema） 
‐ 169 ‐ 
<xs:documentation>每增加1 次装卸损耗率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="StoreRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>采购及保管费率</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PackageRecycleFee" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>包装回收费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Mechs" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>机械</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Mech" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>机械明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent>

【第 177 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 170 ‐ 
<xs:extension base="PractBase"> 
<xs:annotation> 
<xs:documentation>工料（设备）机单价基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="FixedCost" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>不变费用</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="FixedCostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>不变费用明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="FixedCostNo" type="xs:double"> 
<xs:annotation> 
<xs:documentation>不变费用明细编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="FixedCostSum" type="xs:double" use="required">

【第 178 页】
XML 架构（XMLSchema） 
‐ 171 ‐ 
<xs:annotation> 
<xs:documentation>不变费用金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="FixedRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>不变费用系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="VariableCost" maxOccurs="1" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>可变费用</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="VariableCostItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>可变费用明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="VariableCostNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>可变费用消耗编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Consumption" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>消耗量</xs:documentation>

【第 179 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 172 ‐ 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="VariableCostSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>可变费用金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="PractNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单价文件编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单价文件名称</xs:documentation> 
</xs:annotation>

【第 180 页】
XML 架构（XMLSchema） 
‐ 173 ‐ 
</xs:attribute> 
<xs:attribute name="AltitudeRatio" type="xs:double"> 
<xs:annotation> 
<xs:documentation>高海拔基价调整系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TaxLibNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（车船税）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PriceFileNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价依据编码（价格信息）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="EprjInfo" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>项目分段</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="MakeInfo" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>编制信息</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Manage" type="xs:string" use="required">

【第 181 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 174 ‐ 
<xs:annotation> 
<xs:documentation>建设管理单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Designer" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>设计单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Compile" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>编制单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>编制人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileCertNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>编制人证书号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>编制日期</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Review" type="xs:string"> 
<xs:annotation> 
<xs:documentation>复核单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewApprover" type="xs:string" use="required"> 
<xs:annotation>

【第 182 页】
XML 架构（XMLSchema） 
‐ 175 ‐ 
<xs:documentation>复核人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewCertNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>复核人证书号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>复核日期</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Examine" type="xs:string"> 
<xs:annotation> 
<xs:documentation>审核单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineApprover" type="xs:string"> 
<xs:annotation> 
<xs:documentation>审核人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineCertNo" type="xs:string"> 
<xs:annotation> 
<xs:documentation>审核人证书号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineDate" type="xs:dateTime"> 
<xs:annotation> 
<xs:documentation>审核日期</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileExplain" type="xs:string"> 
<xs:annotation> 
<xs:documentation>编制说明</xs:documentation>

【第 183 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 176 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineExplain" type="xs:string"> 
<xs:annotation> 
<xs:documentation>审核说明</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProjectExplain" type="xs:string"> 
<xs:annotation> 
<xs:documentation>工程说明</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Params" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>工程参数</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="PrjArea" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程所在地</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="StartPileNo" type="xs:string"> 
<xs:annotation> 
<xs:documentation>起点桩号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="EndPileNo" type="xs:string"> 
<xs:annotation> 
<xs:documentation>终点桩号</xs:documentation>

【第 184 页】
XML 架构（XMLSchema） 
‐ 177 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="BuildType" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>建设性质</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Terrain" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>地形类别</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RoadGrade" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>公路技术等级</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DesignSpeed" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>设计时速</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Structure" type="xs:integer" use="required"> 
<xs:annotation> 
<xs:documentation>路面结构</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SubgradeWidth" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>路基宽度</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RoadLength" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>路线长度</xs:documentation> 
</xs:annotation>

【第 185 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 178 ‐ 
</xs:attribute> 
<xs:attribute name="BridgeLength" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>桥梁长度</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TunnelLength" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>隧道长度</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="BriTunRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>桥隧比</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InterchangeNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>互通式立交数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="StubLengths" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>支线、联络线长度</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LaneLength" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>辅道、连接线长度</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RisingRate" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>年造价上涨率</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 186 页】
XML 架构（XMLSchema） 
‐ 179 ‐ 
<xs:attribute name="RisingYears" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>上涨计费年限</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="RateNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费率文件编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PractNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工料机单价文件编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Items" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）造价文件</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Item" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>要素项目（清单）表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
</xs:extension> 
</xs:complexContent>

【第 187 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 180 ‐ 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>项目分段名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sums" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>项目分段总造价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Indexs" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>项目造价指标</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="IndexItem" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>指标项</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent>

【第 188 页】
XML 架构（XMLSchema） 
‐ 181 ‐ 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>指标编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>指标名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string"> 
<xs:annotation> 
<xs:documentation>单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Value" type="xs:string"> 
<xs:annotation> 
<xs:documentation>指标值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remark" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence>

【第 189 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 182 ‐ 
<xs:attribute name="CprjName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>建设项目名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CprjType" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价类型编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InvestType" type="xs:string"> 
<xs:annotation> 
<xs:documentation>投资模式</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:schema> 
A.0.3 工程决算成果数据XML Schema 
<?xml version="1.0" encoding="UTF-8" ?> 
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
<xs:complexType name="BaseType"> 
<xs:annotation> 
<xs:documentation>基类元素</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="CustomData" maxOccurs="unbounded" minOccurs="0"> 
<xs:annotation> 
<xs:documentation>自定义数据</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:attribute name="Id" type="xs:string" use="required"> 
<xs:annotation>

【第 190 页】
XML 架构（XMLSchema） 
‐ 183 ‐ 
<xs:documentation>数据内部编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DataName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DataValue" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>数据值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PId" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>父结点ID</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:complexType> 
</xs:element> 
</xs:sequence>    
<xs:attribute name="KeyId" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>实体主键</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:complexType> 
<xs:complexType name="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Items" type="ItemsBase"> 
<xs:annotation>

【第 191 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 184 ‐ 
<xs:documentation>费用要素项目（清单）表</xs:documentation> 
</xs:annotation> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Code" type="xs:string"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit1" type="xs:string"> 
<xs:annotation> 
<xs:documentation>单位2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
<xs:element name="CprjInfo"> 
<xs:annotation> 
<xs:documentation>建设项目</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="SystemInfo" maxOccurs="1" minOccurs="1">

【第 192 页】
XML 架构（XMLSchema） 
‐ 185 ‐ 
<xs:annotation> 
<xs:documentation>基本信息</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>标准名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Version" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>标准版本</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SoftwareName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>软件名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SoftwareVer" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>软件版本</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SoftwareCompany" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>软件公司名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MakeDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>文件生成时间</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 193 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 186 ‐ 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="CprjBasis"> 
<xs:annotation> 
<xs:documentation>建设项目概况</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Cprjbasic"> 
<xs:annotation> 
<xs:documentation>工程概况</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Type" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>项目类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InvestmentMode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>投资模式</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Pilenumber" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>起止桩号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TotalSum" type="xs:double" use="required"> 
<xs:annotation>

【第 194 页】
XML 架构（XMLSchema） 
‐ 187 ‐ 
<xs:documentation>决算总金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InstallationSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>决算建安费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PlanStartDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>计划开始时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PlanEndDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>计划竣工时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ActualStartDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>实际开始时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ActualEndDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>实际竣工时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DesignOrgan" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>初步设计审批机关</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DesigDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>初步设计审批时间</xs:documentation>

【第 195 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 188 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DesigNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>初步设计审批文号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Manage" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>建设项目法人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="CprjIndexs" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>主要技术指标</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CprjIndex" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>主要技术指标明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>指标编码</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 196 页】
XML 架构（XMLSchema） 
‐ 189 ‐ 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>指标名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Value" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>指标值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="CprjCost" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用情况</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CprjCost" maxOccurs="1" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>费用情况明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation>

【第 197 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 190 ‐ 
<xs:documentation>费用编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>费用名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="SjgsSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>批准概预算</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="GcjsSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>工程决算</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MoreLess" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>净增减</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="CprjNums"> 
<xs:annotation> 
<xs:documentation>主要工程量</xs:documentation> 
</xs:annotation>

【第 198 页】
XML 架构（XMLSchema） 
‐ 191 ‐ 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="CprjNum"> 
<xs:annotation> 
<xs:documentation>主要工程量明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>主要分部工程编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>主要分部工程名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DesignNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>设计工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="FinishNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>完成工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 199 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 192 ‐ 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="CompileApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>编制人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>编制时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>复核人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>复核时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>审核人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineDate" type="xs:dateTime" use="required">

【第 200 页】
XML 架构（XMLSchema） 
‐ 193 ‐ 
<xs:annotation> 
<xs:documentation>审核时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="FinancialAccounts"> 
<xs:annotation> 
<xs:documentation>财务总决算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="FinancialAccount"> 
<xs:annotation> 
<xs:documentation>财务决算明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="No" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>序号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MoneySource" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>资金来源</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation>

【第 201 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 194 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MoneyOccupy" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>资金占用</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="ContrastTables"> 
<xs:annotation> 
<xs:documentation>工程总决算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="ContrastTable"> 
<xs:annotation> 
<xs:documentation>工程总决算明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType">

【第 202 页】
XML 架构（XMLSchema） 
‐ 195 ‐ 
<xs:sequence> 
<xs:element name="Gkgs"> 
<xs:annotation> 
<xs:documentation>估算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>估算金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Codes" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>对应要素费用项目（清单）编码</xs:documentation>

【第 203 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 196 ‐ 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Sjgs"> 
<xs:annotation> 
<xs:documentation>概算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>概算金额</xs:documentation>

【第 204 页】
XML 架构（XMLSchema） 
‐ 197 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Codes" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>对应要素费用项目（清单）编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Sgys"> 
<xs:annotation> 
<xs:documentation>预算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation>

【第 205 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 198 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>预算金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Codes" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>对应要素费用项目（清单）编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Gcht"> 
<xs:annotation> 
<xs:documentation>工程合同</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation>

【第 206 页】
XML 架构（XMLSchema） 
‐ 199 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合同金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Codes" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>对应合同项目节编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Gcjs"> 
<xs:annotation> 
<xs:documentation>决算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>数量2</xs:documentation>

【第 207 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 200 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>决算金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Codes" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>对应要素费用项目（清单）编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>分项编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程或费用名称</xs:documentation> 
</xs:annotation>

【第 208 页】
XML 架构（XMLSchema） 
‐ 201 ‐ 
</xs:attribute> 
<xs:attribute name="Unit1" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit2" type="xs:string"> 
<xs:annotation> 
<xs:documentation>单位2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="CprjInvest"> 
<xs:annotation> 
<xs:documentation>建设项目前期投资控制</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Gkgs" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>工可估算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence>

【第 209 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 202 ‐ 
<xs:element name="GkgsItem"> 
<xs:annotation> 
<xs:documentation>工可估算项目节</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="SystemCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>估算项目节内部编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>Num2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required">

【第 210 页】
XML 架构（XMLSchema） 
‐ 203 ‐ 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Sjgs"> 
<xs:annotation> 
<xs:documentation>初步设计概算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="SjgsItem"> 
<xs:annotation> 
<xs:documentation>初步设计概算项目节</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="SystemCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>概算项目节内部编码</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 211 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 204 ‐ 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>Num2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Sgys"> 
<xs:annotation>

【第 212 页】
XML 架构（XMLSchema） 
‐ 205 ‐ 
<xs:documentation>施工图预算</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="SgysItem"> 
<xs:annotation> 
<xs:documentation>施工图预算项目节</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="SystemCode" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>预算项目节内部编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量1</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>Num2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price1" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价1</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 213 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 206 ‐ 
<xs:attribute name="Price2" type="xs:double"> 
<xs:annotation> 
<xs:documentation>单价2</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="SummaryTables"> 
<xs:annotation> 
<xs:documentation>建设项目建安工程决算汇总表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="SummaryTable"> 
<xs:annotation> 
<xs:documentation>建设项目建安工程决算明细</xs:documentation> 
</xs:annotation>

【第 214 页】
XML 架构（XMLSchema） 
‐ 207 ‐ 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="TotalNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合计工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TotalSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合计金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AveragePrice" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>平均单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="ChangeSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>变更引起调整合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MpriceSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>工程项目调价合计</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 215 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 208 ‐ 
<xs:attribute name="ClaimSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>工程项目索赔合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DayworkSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>计日工支出合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TotalSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InstallationSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>建安决算总金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="EquipmentSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>设备费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="PurchasecostTables"> 
<xs:annotation> 
<xs:documentation>设备、工具、器具及家具购置费支出汇总表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType">

【第 216 页】
XML 架构（XMLSchema） 
‐ 209 ‐ 
<xs:sequence> 
<xs:element name="PurchasecostTable"> 
<xs:annotation> 
<xs:documentation>设备、工具、器具及家具购置费支出明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="No" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>序号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程或费用名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ContractNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>合同编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Unit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation>

【第 217 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 210 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ContractSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合同金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CostSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>支出金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>差额说明</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="OthercostTables"> 
<xs:annotation> 
<xs:documentation>工程建设其他费用支出汇总表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="OthercostTable"> 
<xs:annotation>

【第 218 页】
XML 架构（XMLSchema） 
‐ 211 ‐ 
<xs:documentation>工程建设其他费用支出明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="No" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>序号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程或费用名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ContractNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>合同编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ContractName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>合同名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ContractSum" type="xs:double" use="required">

【第 219 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 212 ‐ 
<xs:annotation> 
<xs:documentation>合同金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CostSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>支出金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>差额说明</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="EprjInfo" maxOccurs="unbounded" minOccurs="1"> 
<xs:annotation> 
<xs:documentation>工程项目</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="EprjIndexs"> 
<xs:annotation> 
<xs:documentation>工程项目技术指标</xs:documentation> 
</xs:annotation> 
<xs:complexType>

【第 220 页】
XML 架构（XMLSchema） 
‐ 213 ‐ 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="EprjIndex"> 
<xs:annotation> 
<xs:documentation>工程项目技术指标明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Code" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>指标编码</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>指标名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Value" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>指标值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="EprjGcjs"> 
<xs:annotation>

【第 221 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 214 ‐ 
<xs:documentation>工程项目工程决算文件</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="EprjNums"> 
<xs:annotation> 
<xs:documentation>决算工程量登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Quantities"> 
<xs:annotation> 
<xs:documentation>决算清单工程量</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:sequence> 
<xs:element name="Quantitie"> 
<xs:annotation> 
<xs:documentation>决算清单工程量明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Name" type="xs:string" use="prohibited"> 
<xs:annotation> 
<xs:documentation>工程量名称</xs:documentation> 
</xs:annotation>

【第 222 页】
XML 架构（XMLSchema） 
‐ 215 ‐ 
</xs:attribute> 
<xs:attribute name="Pilenumber" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>起止桩号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Area" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>位置</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DesignNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>原设计数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LeakageNum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>设计错漏数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OtherNum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>其他原因增减数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeNum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>变更数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AccountsNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>决算数量</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 223 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 216 ‐ 
<xs:attribute name="DrawingNo" type="xs:string"> 
<xs:annotation> 
<xs:documentation>图纸编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="DesignNums" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>原设计数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="LeakageNums" type="xs:double"> 
<xs:annotation> 
<xs:documentation>设计错漏数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="OtherNums" type="xs:double"> 
<xs:annotation> 
<xs:documentation>其他原因增减数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeNums" type="xs:double"> 
<xs:annotation> 
<xs:documentation>变更数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="AccountsNums" type="xs:double" use="required">

【第 224 页】
XML 架构（XMLSchema） 
‐ 217 ‐ 
<xs:annotation> 
<xs:documentation>决算数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="EprjAccounts"> 
<xs:annotation> 
<xs:documentation>工程决算表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="EprjAccount"> 
<xs:annotation> 
<xs:documentation>项目分段决算明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="ContractNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合同工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 225 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 218 ‐ 
<xs:attribute name="ChangeNum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>变更工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>核算工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PayNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>支付工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ContractSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合同金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PaySum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>支付金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MoreLess" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>差量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string">

【第 226 页】
XML 架构（XMLSchema） 
‐ 219 ‐ 
<xs:annotation> 
<xs:documentation>差量原因</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="ChangeSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>变更引起调整合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="MpriceSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>工程项目调价合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ClaimSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>工程项目索赔合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="DayworkSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>计日工支出合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="UnforeseeableSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>不可预见费（暂定金额）</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="TotalSum" type="xs:double" use="required"> 
<xs:annotation>

【第 227 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 220 ‐ 
<xs:documentation>决算金额合计</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InstallationSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>建安决算总金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="EquipmentSum" type="xs:double"> 
<xs:annotation> 
<xs:documentation>设备费</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="EprjContracts"> 
<xs:annotation> 
<xs:documentation>工程合同登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Contracts"> 
<xs:annotation> 
<xs:documentation>工程合同</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Contract"> 
<xs:annotation> 
<xs:documentation>工程合同明细</xs:documentation>

【第 228 页】
XML 架构（XMLSchema） 
‐ 221 ‐ 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Type" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>合同类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element>

【第 229 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 222 ‐ 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="ChangeDesigns"> 
<xs:annotation> 
<xs:documentation>变更设计登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="ChangeItems"> 
<xs:annotation> 
<xs:documentation>变更项目</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="ChangeItem"> 
<xs:annotation> 
<xs:documentation>变更明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>变更数量</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 230 页】
XML 架构（XMLSchema） 
‐ 223 ‐ 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>变更单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>变更金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="ChangeNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>变更编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ProjectName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ApprovedUnit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>批准单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ApprovedNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>批准文号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Comments" type="xs:string">

【第 231 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 224 ‐ 
<xs:annotation> 
<xs:documentation>设计单位意见</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>变更原因</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="ChangeSums"> 
<xs:annotation> 
<xs:documentation>变更引起调整金额登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="ChangeSum"> 
<xs:annotation> 
<xs:documentation>变更引起调整金额明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation>

【第 232 页】
XML 架构（XMLSchema） 
‐ 225 ‐ 
<xs:attribute name="ContractPrice" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>合同工程单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangePrice" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>调整单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Dvalue" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价差值</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeNum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>调整单价支付数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>调整金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>调整原因</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension>

【第 233 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 226 ‐ 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Mprices"> 
<xs:annotation> 
<xs:documentation>工程项目调价登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="PriceIndex"> 
<xs:annotation> 
<xs:documentation>价格指数调价明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="No" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>序号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeData" type="xs:date" use="required"> 
<xs:annotation> 
<xs:documentation>调整时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeRatio" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>综合调价系数</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PaySum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>累计支付额</xs:documentation>

【第 234 页】
XML 架构（XMLSchema） 
‐ 227 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>调价金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="MaterialPrice"> 
<xs:annotation> 
<xs:documentation>材料价格信息调价明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="No" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>序号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeContent" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>调整内容</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="PriceDifference" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>材料价差</xs:documentation>

【第 235 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 228 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>材料数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ChangeSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>调价金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string"> 
<xs:annotation> 
<xs:documentation>备注</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Claims"> 
<xs:annotation> 
<xs:documentation>工程项目索赔登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Claim"> 
<xs:annotation>

【第 236 页】
XML 架构（XMLSchema） 
‐ 229 ‐ 
<xs:documentation>索赔明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>索赔项目</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ClaimSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>索赔金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Remarks" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>Remarks</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompensateSum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>赔偿金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ApprovedNo" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>批准文号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension>

【第 237 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 230 ‐ 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Dayworks"> 
<xs:annotation> 
<xs:documentation>计日工支出金额登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Daywork"> 
<xs:annotation> 
<xs:documentation>计日工支出明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="Type" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>计日工类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 238 页】
XML 架构（XMLSchema） 
‐ 231 ‐ 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="EndingProject"> 
<xs:annotation> 
<xs:documentation>收尾工程登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Endings"> 
<xs:annotation> 
<xs:documentation>收尾工程</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Ending"> 
<xs:annotation> 
<xs:documentation>收尾工程明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent>

【第 239 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 232 ‐ 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>工程量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="Name" type="xs:string"> 
<xs:annotation> 
<xs:documentation>工程名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent>

【第 240 页】
XML 架构（XMLSchema） 
‐ 233 ‐ 
</xs:complexType> 
</xs:element> 
<xs:element name="Scraps"> 
<xs:annotation> 
<xs:documentation>报废工程登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Scrap"> 
<xs:annotation> 
<xs:documentation>报废工程明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:attribute name="No" use="required"> 
<xs:annotation> 
<xs:documentation>序号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程内容或名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>工程数量</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>支出金额</xs:documentation> 
</xs:annotation>

【第 241 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 234 ‐ 
</xs:attribute> 
<xs:attribute name="Rremarks" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>原因</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
<xs:element name="Payments"> 
<xs:annotation> 
<xs:documentation>工程支付情况登记表</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="BaseType"> 
<xs:sequence> 
<xs:element name="Payment"> 
<xs:annotation> 
<xs:documentation>支付项目明细</xs:documentation> 
</xs:annotation> 
<xs:complexType> 
<xs:complexContent> 
<xs:extension base="ItemsBase"> 
<xs:annotation> 
<xs:documentation>费用要素项目（清单）基类</xs:documentation> 
</xs:annotation> 
<xs:attribute name="Num" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>数量</xs:documentation>

【第 242 页】
XML 架构（XMLSchema） 
‐ 235 ‐ 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Price" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>单价</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Sum" type="xs:double" use="required"> 
<xs:annotation> 
<xs:documentation>金额</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="No" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程项目编号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Name" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>工程项目名称</xs:documentation> 
</xs:annotation>

【第 243 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 236 ‐ 
</xs:attribute> 
<xs:attribute name="Pilenumber" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>起止桩号</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="Type" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>项目类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ConstructionUnit" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>施工单位</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>编制人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="CompileDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>编制时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>复核人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ReviewDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>复核时间</xs:documentation> 
</xs:annotation> 
</xs:attribute>

【第 244 页】
XML 架构（XMLSchema） 
‐ 237 ‐ 
<xs:attribute name="ExamineApprover" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>审核人</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="ExamineDate" type="xs:dateTime" use="required"> 
<xs:annotation> 
<xs:documentation>审核时间</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:sequence> 
<xs:attribute name="cprjName" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>建设项目名称</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="cprjType" type="xs:string" use="required"> 
<xs:annotation> 
<xs:documentation>造价类型</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
<xs:attribute name="InvestType" type="xs:string"> 
<xs:annotation> 
<xs:documentation>投资模式</xs:documentation> 
</xs:annotation> 
</xs:attribute> 
</xs:extension> 
</xs:complexContent> 
</xs:complexType> 
</xs:element> 
</xs:schema>

【第 245 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 238 ‐ 
本标准用词用语说明 
 
 
1  本标准执行严格程度的用词，采用下列写法： 
1)  表示很严格，非这样做不可的用词，正面词采用“必须”，反面词采用“严禁”； 
2)  表示严格，在正常情况下均应这样做的用词，正面词采用“应”，反面词采用“不
应”或“不得”； 
3)  表示允许稍有选择，在条件许可时首先应这样做的用词，正面词采用“宜”，反
面词采用“不宜”； 
4)  表示有选择，在一定条件下可以这样做的用词，采用“可”。 
 
2  引用标准的用语采用下列写法： 
1)  在标准总则中表述与相关标准的关系时，采用“除应符合本标准的规定外，尚
应符合国家和行业现行有关标准的规定”。 
2）  在标准条文及其他规定中，当引用的标准为国家标准和行业标准时，表述为“应
符合《××××××》(×××)的有关规定”。 
3）  当引用本标准中的其他规定时，表述为“应符合本标准第×章的有关规定”、
“应符合本标准第×.×节的有关规定”、“应符合本标准第×.×.×条的有关规定”或“应
按本标准第×.×.×条的有关规定执行”。

【第 246 页】
本标准引用名录 
‐ 239 ‐ 
本标准引用名录  
 
本标准主要依据以下法律法规及标准： 
1《交通信息基础数据元》（JT/T 697） 
2《公路工程建设项目造价文件编制导则》（JTG 3810-2017） 
3《公路工程建设项目投资估算编制办法》（JTG 3820-2018） 
4《公路工程建设项目概算预算编制办法》（JTG 3830-2018） 
5《公路工程估算指标》（JTG/T 3821-2018） 
6《公路工程概算定额》（JTG/T 3831-2018） 
7《公路工程预算定额》（JTG/T 3832-2018） 
8《公路工程机械台班费用定额》（JTG/T 3833-2018） 
9《信息技术可扩展置标语言（XML）1.0》（GB/T 18793-2002） 
10《软件开发与文档编制》（SJ 20778-2000）

【第 247 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 240 ‐ 
 
《公路工程建设项目造价数据标准》 
 
（JTG/T 3812—2020） 
 
条文说明

【第 248 页】
条文说明 
‐ 241 ‐ 
1 总则 
1.0.1 根据《公路工程建设项目造价文件管理导则》（JTG 3810-2017）相关规定，造
价依据指用于各阶段造价文件所依据的办法、规则、定额、费用标准、造价指标以及其
他相关的基价标准。如《公路养护预算编制办法》、《公路养护工程预算定额》等。造价
文件指项目建议、工程可行性研究、初步设计、施工图设计、招标、施工、交通、竣工
等各阶段造价类文件的统称，包括投资估算、设计概算、施工图预算、工程量清单、工
程量清单预算、合同工程量清单、计量与支付、工程变更费用、造价管理台账、工程结
算、工程竣工决算等文件。 
 
1.0.5 为适应电子招标投标，相关管理部门宜在本数据标准基础上，制定相应的补充
规定。 
 
3 基本规定 
3.0.2 定额资源、费率标准库、要素费用项目（清单）表库、车船税费库、人工单价、
规费费率、利润率、税率八类造价依据可整体一次性导出形成完整的电子数据文件，也
可导出其中的一类形成单独的电子数据文件，价格信息只能单独导出形成电子数据文件。
造价成果只能按造价类型单独导出形成电子数据文件。 
3.0.3 四舍五入示例：数值1.5342 和1.5346 保留2 位小数的结果均为1.53，数值1.5352
和1.5353 保留2 位小数的结果均为1.54。 
3.0.4 编制造价过程中的不同类型数据的计算精度应符合以下规定： 
1 费率计算过程中，费率值保留3 位小数；在加权计算及内插计算过程中不作精度
舍入，最后保留3 位小数。 
2 工料机消耗数量=定额工程数量×定额消耗量，结果保留3 位小数； 
3 工料机单价计算应符合以下规定： 
1）运杂费按“（吨·公里运价×运距）×毛重系数+装卸费用+其它费用”公式计算，

【第 249 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 242 ‐ 
结果保留2 位小数；如有多方案运输时，运杂费合计=∑运杂费×加权系数，结果保留2
位小数。 
2）自采及自办运输材料计算精度参照建安费计算规则及精度要求。 
3）材料预算单价按“（材料原价+运杂费）×（1+场外运输损耗率）×（1+采购及保
管费率）-包装品回收价值”公式计算，结果保留2 位小数。 
4）机械台班单价计算应符合以下规定： 
——不变费用=定额不变费用×调整系数，结果保留2 位小数； 
——各项可变费用=定额消耗量×单价，结果保留2 位小数； 
——可变费用=∑各项可变费用+车船税，结果保留2 位小数； 
——台班单价=不变费用+可变费用，结果保留2 位小数。 
4 金额计算应符合以下规定： 
1）基础计算应符合以下规定： 
——人工费=∑人工消耗量×人工单价，结果取整； 
——定额人工费=∑人工消耗量×人工基价，结果取整； 
——材料费=∑材料消耗量×材料预算单价，结果取整； 
——定额材料费=∑材料消耗量×材料基价，结果取整； 
——施工机械使用费=∑机械台班消耗量×机械台班预算单价，结果取整； 
——定额施工机械使用费=∑机械台班消耗量×机械台班基价，结果取整； 
——机械人工费=机械台班定额中人工消耗量×机械工人工预算单价×台班消耗量
×定额工程数量，结果取整； 
——人工费（含施工机械人工费）=人工费+施工机械人工费，结果取整。 
2）直接费计算应符合以下规定： 
——工料机金额=工料机各项的单价×工料机消耗数量，结果取整； 
——直接费=∑工料机金额，结果取整。 
3）定额直接费计算应符合以下规定： 
——工料机金额=工料机各项的基价×数量，结果取整； 
——定额直接费=∑工料机金额，结果取整。

【第 250 页】
条文说明 
‐ 243 ‐ 
4）措施费计算应符合以下规定： 
——措施费Ⅰ=定额直接费×施工辅助费费率，结果取整； 
——措施费Ⅱ=（定额人工费+定额施工机械使用费）×其余措施费综合费率，结果
取整。 
5）企业管理费=定额直接费×企业管理费综合费率，结果取整。 
6）规费=各类工程人工费（含施工机械人工费）×规费综合费率，结果取整。 
7）利润=（定额直接费+措施费+企业管理费）×利润率，结果取整。 
8）税金=（直接费+设备购置费+措施费+企业管理费+规费+利润）×税率，结果取整。 
9）设备购置费计算应符合以下规定： 
——设备购置费=设备数量×设备预算单价，结果取整； 
——定额设备购置费=设备数量×设备基价，结果取整； 
——设备税金=设备购置费×税率，结果取整； 
——设备费=设备购置费+设备税金，结果取整。 
——定额设备费=定额设备购置费+设备税金，结果取整； 
10）专项费用计算应符合以下规定： 
——专项费用=施工场地建设费+安全生产费，结果取整； 
——施工场地建设费=（定额直接费+措施费+企业管理费+规费+利润+税金）×累进
费率，结果取整； 
——安全生产费=建筑安装工程费（不含安全生产费本身）×安全生产费费率，结果
取整。 
11）定额建筑安装工程费计算应符合以下规定： 
——定额建筑安装工程费Ⅰ=定额直接费+定额设备购置费+措施费+企业管理费+规
费+利润+税金+专项费用，结果取整； 
——定额建筑安装工程费Ⅱ=定额直接费+定额设备购置费×40%+措施费+企业管理
费+规费+利润+税金+专项费用，结果取整。 
12）建筑安装工程费=直接费+设备购置费+措施费+企业管理费+规费+利润+税金+专
项费用，结果取整。

【第 251 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 244 ‐ 
13）其他费用计算应符合以下规定： 
（1）建设单位（业主）管理费、建设项目信息化费、工程监理费、设计文件审查费、
建设项目前期工作费、联合试运转费采用的计算基数为“定额建筑安装工程费Ⅱ”。 
（2）其他各项费用计算后取整。 
 
4 造价依据数据标准 
4.3 造价依据基类 
数据类型即属性类型，指用于界定一个属性所要保存的数据的类型，包括字符型、
数值型、日期型、逻辑型、枚举型。属性类型根据需要选择确定。 
1 字符型（String）：可以保存任何类型的数据。 
2 数值型（Integer）：由数字组成，用于代表一个属性的数值； 
3 数值型（Double）：由数字组成，用于代表一个属性的数值，可含有小数点。 
4 日期型（Datetime）：用于保存日期数据，格式为YYYY-MM-DD，如：2017-08-24。 
5 逻辑型（Boolean）：用于判断事件“真”或“假”的值，分别以“0”和“1”
表示“假”和“真”。 
6 枚举型（Integer）：仅可使用特定的值作为属性值。 
4.4 定额资源 
4.4.1 本标准所指“工料机”包含“设备”。 
4.4.5 为表达数据之间的关联（对应）关系，在部分数据元素中设置了名为Uuid 的
属性，含义说明为“***唯一编码”，XML 文档中应保证该内部编码属性取值在同一要素
数据集中的唯一性。 
4.6 要素费用项目(清单) 
1 要素费用项目(清单)指贯穿工程造价管理全过程，具有固定统一的编码、工程或费
用名称、统计单位、工作内容、计量规则等特性，并为反映公路工程造价总体情况而规
定的通用性的基本费用项目。本标准要素费用项目（清单）引用《公路工程建设项目投

【第 252 页】
条文说明 
‐ 245 ‐ 
资估算编制办法》附录B 投资估算项目表”和“《公路工程建设项目概算预算编制办法》
附录B 概预算项目表”以及“《公路工程标准施工招标文件范本》第五章工程量清单表”。 
6 数据编码标准 
6.2 造价依据编码 
6.2.1 造价依据编码
1 造价依据编码编码示例 
造价依据编码前缀 
造价依据名称 
备注 
GSBB-000000-部公告[2018]第86 号-** 
公路工程建设项目投资估算编制办法 
部颁标准
GYSBB-000000-部公告[2018]第86 号-** 
公路工程建设项目概算预算编制办法 
部颁标准
GSZB-000000-部公告[2018]第86 号-** 
公路工程估算指标 
部颁标准
GSDE-000000-部公告[2018]第86 号-** 
公路工程概算定额 
部颁标准
YSDE-000000-部公告[2018]第86 号-** 
公路工程预算定额 
部颁标准
GLJ-000000-部公告[2018]第86 号-** 
2018 工料机库 
部颁标准
GLJJJ-000000-部公告[2018]第86 号-** 
2018 工料机基价库 
部颁标准
GSFL-000000-部公告[2018]第86 号-** 
2018 估算费率 
部颁标准
GYSFL-000000-部公告[2018]第86 号-** 
2018 概预算费率 
部颁标准
GSFX-000000-部公告[2018]第86 号-** 
2018 估算分项 
部颁标准
GYSFX-000000-部公告[2018]第86 号-** 
2018 概预算分项 
部颁标准
CCSBZ-530000-云交建设[2019]34 号-** 
2018 车船税标准 
云南 
JGXX-530000-云交造价[2018]128 号-** 
2018 年云南第6 期价格信息 
云南 
2 行政区划代码表仅列出省（自治区、直辖市）级代码，市（州、地区）、县（区）
级代码参见全国行政区划代码表。 
6.4 费率编码 
6.4.1 费率类别编码为相应取费类别名称汉语拼音首字母缩写，若编码冲突（编码值
重复）则从第 1 个字符起使用拼音全拼代替拼音首字母，直至编码值不冲突为止。例如： 
“雨季施工增加费费率”和“夜间施工增加费费率”使用汉语拼音首字母缩写作为取费
类别编码时均为 YJSGZJFFL（编码值重复），则“雨季施工增加费费率”和“夜间施工增

【第 253 页】
公路工程建
加费费率
6.5 工料
6.5.
6.7 定额
6.7.
1 概
一张表
上）”
2 估
额子目
 
7 其他
本标
估算编
B06‐200
B06‐01‐
（JTG B
时，除按
建设项目造价
率”分别使
料机编码 
1 工料机编
额子目编码
1 定额子目
概算定额“
“伐树、挖
。 
估算指标“
“挖、装土
他说明 
标准按现行
制办法》（
07）、《公路
‐2007）、
《公
B06‐03‐2007
按本标准规
数据标准（JT
使用“YUJSG
编码组成示例
图
码 
目编码示例：
“1-1-1-1”
挖根、除草
“1-1-1”指
土方”子目
行的公路工
（JTG  M20‐
路工程估算
公路工程预算
7）编制的估
规定的数据
G/T 3812—20
GZJFFL”和
例如图6.5
图6.5.1HPB3
 
指：第一章
、清除表土
指：第一章
。 
程建设计价
2011）、《公
算指标》(
算定额》
（JT
估算、概算
结构及内容
020） 
‐ 246 
和“YEJSGZJF
.1 所示。
300 钢筋的编
章“路基工
土”-第一条
“路基工程
价标准编制
公路工程基
(JTG  M21‐2
TG/T B06‐0
算、预算及
容执行外，
‐ 
FFL”作为取
编码组成示意
工程”-第一
条定额子目
程”-第一章
，如采用
基本建设项
2011)、《公
2‐2007）、
《
清单历史造
缺少的编码
取费类别编
意图： 
一节“路基土
“伐树及挖
章表“挖、装
《公路工程
项目概算预算
公路工程概
公路工程机
造价数据使
码及内容按
编码。 
土、石方工
挖根（直径
装土方”-第
程基本建设项
算编制办法
概算定额》
机械台班费
使用本标准导
按以下规定执
工程”-第
径10cm 以
第一条定
项目投资
法》（JTG 
》（JTG/T 
费用定额》
导出XML
执行。

【第 254 页】
条文说明 
‐ 247 ‐ 
7.1 元素属性 
按本标准导出xml 数据时，如结构元素属性为必填，但历史造价成果数据中没有的
内容可以不填，如项目造价依据编码、费用列表中的基价、工程决算建设项目中的财务
总决算等，但造价依据名称必须填写。 
7.2 编码标准 
7.2.1“表6.3.1 估算编制办法对应工程类别编码”增加如下编码。 
编码 
工程类别名称 
备注 
RGTF 
人工土方 
 
JXTF 
机械土方 
 
YS 
汽车运输 
采用18 编办“运输”对应编码 
TGSF 
人工石方 
 
JXSF 
机械石方 
 
GJLM 
高级路面 
 
QTLM 
其他路面 
 
GZW3(BJY) 
构造物Ⅲ（不计雨） 
 
GZW3(BJYY 
构造物Ⅲ（不计雨夜） 
 
7.2.2“表6.3.2 概算预算编制办法对应工程类别编码”增加如下编码。 
编码 
工程类别名称 
备注 
RGTF 
人工土方 
 
JXTF 
机械土方 
 
YS 
汽车运输 
采用18 编办“运输”对应编码 
TGSF 
人工石方 
 
JXSF 
机械石方 
 
GJLM 
高级路面 
 
QTLM 
其他路面 
 
GZW3(BJY) 
构造物Ⅲ（不计雨） 
 
GZW3(BJYY 
构造物Ⅲ（不计雨夜） 
 
7.2.3“表6.4.1 费率类别编码”增加如下编码。 
费率类别编码 
费率类别名称 
SGBZHYAQCSFFL 
施工标准化与安全措施费费率 
LSSSFFL 
临时设施费费率

【第 255 页】
公路工程建设项目造价数据标准（JTG/T 3812—2020） 
‐ 248 ‐ 
费率类别编码 
费率类别名称 
JJFFL 
间接费费率 
QTGCFFL1 
其他工程费费率Ⅰ 
QTGCFFL2 
其他工程费费率Ⅱ 
7.2.4“表6.4.2-3 高原地区施工增加费费率取值参数编码”增加如下编码。 
取值参数编码 
高原地区施工取值参数名 
8 
1501~2000 
7.2.5“表6.4.2-7 其他费率取值参数编码”增加如下编码。 
取值参数编码或值 
费率类别名称 
0 表示为不计，1 表示计 
临时设施费费率 
0 表示为不计，1 表示计 
施工标准化与措施费费率 
7.2.6 工料机编码 
工料机编码采用《公路工程预算定额》（JTG/T B06‐02‐2007）附录四及《公路工程机
械台班费用定额》（JTG/T B06‐03‐2007）中的编码。 
7.2.7“表6.6.1 施工机械不变费用明细编码”完善如下内容。 
编码 
不变费用明细名称 
备注 
0 
折旧费 
 
1 
大修理费 
采用18 编办“检修费”对应编码 
2 
经常修理费 
采用18 编办“维护费”对应编码 
3 
安装拆卸及辅助设施费 
采用18 编办“安拆辅助费” 对应编码 
7.2.8 要素费用项目编码即估概预项目编码，项、目、节、细目采用数字编码，项、
目、节、细目间采用“-”相连。 
7.2.9“表6.11.1 费用构成明细编码及计算取值引用规则”增加如下编码。 
编码 
费用构成明细名称 
计算取值引用规则 
ZJGCF 
直接工程费 
{ZJGCF} 
ZJF07 
直接费 
{ZJF07} 
JJF 
间接费 
{JJF} 
CSF 
措施费(其他工程费) 
{CSF} 
CSF1 
措施费Ⅰ（其他工程费Ⅰ） 
{CSF1} 
CSF2 
措施费Ⅱ（其他工程费Ⅱ） 
{CSF2}
