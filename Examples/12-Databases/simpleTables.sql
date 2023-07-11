CREATE DATABASE [steve]
GO

USE [steve]
GO

/****** Object:  Table [dbo].[users]    Script Date: 11/07/2023 12:36:45 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[users](
	[id] [int] NOT NULL,
	[firstname] [varchar](50) NULL,
	[lastname] [varchar](50) NOT NULL,
	[age] [int] NULL,
	[phone] [varchar](30) NOT NULL,
	[postcode] [varchar](8) NOT NULL,
 CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

insert into users values(1,'Steve','Shilling',42,'555-1234','NW1 4RG');
insert into users values(2,'Hadron','Colida',23,'555-9999','NW1 3PQ');
insert into users values(3,'Kat','Aliverdead',32,'555-9876','NW1 2OP');